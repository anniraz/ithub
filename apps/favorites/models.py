from django.db import models

# Create your models here.
from apps.users.models import User
# from django.contrib.auth.models import User



class Favorite(models.Model):
    
    to_user=models.ForeignKey(User,on_delete=models.CASCADE ,related_name='to_user')
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.to_user.username}'

    class Meta:
        unique_together = (('to_user', 'user',),)