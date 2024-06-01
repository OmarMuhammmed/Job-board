from django.db import models

# Create your models here.

class Info(models.Model):
    place = models.CharField( max_length=50)
    phone_number = models.CharField( max_length=11)
    email_support = models.EmailField( max_length=254)
    
    def __str__(self):
        return self.email_support
    