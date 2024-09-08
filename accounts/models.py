from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    city = models.ForeignKey('City', related_name='user_city', on_delete=models.CASCADE ,blank=True, null=True)
    phone_number = models.CharField( max_length=15)
    image = models.ImageField( upload_to='profile/',blank=True, null=True)
    reset_password_token = models.CharField(max_length=50,default="",blank=True)
    reset_password_expire = models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return str(self.user)
    
    
@receiver(post_save, sender=User)    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)    

    
class City(models.Model):
    
    name = models.CharField( max_length=50)

    def __str__(self):
       return self.name
   