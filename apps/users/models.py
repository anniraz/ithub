from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.contrib.auth.models import User

# Create your models here.

class Direction(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,blank=True, related_name='children')

    def __str__(self):
        if not self.parent:
            return f'{self.title}'
        else:
            return f'{self.parent} -> {self.title}' 

    class Meta:
        verbose_name_plural = 'Направления'
        verbose_name= 'Направление'

class User(AbstractUser):
    
    CHOICES = (
        ('Developer', 'Developer'),
        ('Customer', 'Customer'),
    )
    email=models.EmailField( blank=True,null=True,unique=True)
    
    
    REQUIRED_FIELDS=['email']

    def __str__(self):
        return f'{self.username}'


    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name= 'Пользователь'

class Additional_info(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_info')
    first_name=models.CharField(max_length=50,verbose_name='Имя')
    last_name=models.CharField(max_length=50,verbose_name='Фамилия')
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True, verbose_name='Аватарка')
    phone = models.IntegerField(validators=[MinValueValidator(9), MaxValueValidator(12)], null=True, blank=True, verbose_name='Телефон')
    description=models.TextField()

    def __str__(self):
        return f'{self.user.username}'

class Customer(models.Model):
    CUSTOMER_CHOICE=(
        ('Личный клиент','Личный клиент'),
        ('Компания','Компания'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    from_choice=models.CharField(max_length=50,choices=CUSTOMER_CHOICE)
    # user.customer = True

    def __str__(self):
        return f'{self.user}{self.from_choice}'

    class Meta:
        verbose_name_plural = 'Заказчики'
        verbose_name = 'Заказчик'



class Developer(models.Model):
    DEV_LEVEL=(
        ('Junior','Junior'),
        ('Middle','Middle'),
        ('Senior','Senior'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='developer')
    # user.developer = True

    direction = models.ManyToManyField(Direction,null=True,blank=True,verbose_name='Напавление')
    level=models.CharField(max_length=50,choices=DEV_LEVEL, verbose_name='Уровень')
    about=models.TextField(verbose_name='О себе')


    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name_plural = 'Разработчики'
        verbose_name= 'Разработчик'





# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.group == 'developer':
#             Developer.objects.create(user=instance)
#         elif instance.group == 'customer':
#             Customer.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.group == 'developer':
#         instance.developer.save()
#     elif instance.group == 'customer':
#         instance.customer.save()



class Reviews(models.Model):

    RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    
    auth=models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_auth')
    text = models.TextField()
    rating = models.IntegerField(choices=RATING ,blank=True, null=True)
    time_pub = models.DateTimeField(auto_now_add=True)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='reviews_to_user')
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True ,related_name='children')

    def __str__(self):
        return f"{self.auth} - {self.to_user.username} {self.text}"

    class Meta:

        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering=['pk']

