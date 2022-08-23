from django.db import models
from apps.users.models import User


class MakeOrder(models.Model):
    user = models.ForeignKey(User, related_name='user_make_order', on_delete=models.CASCADE)
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return f'I am: {self.user} title:{self.title}'

class Order(models.Model):
    to_user = models.ForeignKey(MakeOrder, related_name='user_order', on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE ,related_name='from_user_order')

    def __str__(self):
        return f'{self.to_user.username}'
    
    # class Meta:
        # unique_together = (('to_user', 'user',),)

    