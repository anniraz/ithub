from django.db import models
from apps.users.models import User

# Create your models here.

class Order(models.Model):
    to_user = models.ForeignKey(User, related_name='user_order', on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE ,related_name='from_user_order')

    def __str__(self):
        return f'{self.to_user.username}'