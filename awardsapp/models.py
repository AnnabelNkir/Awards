from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length =30,null=True)
    email = models.EmailField(max_length =50,null=True)
    pro_photo = models.ImageField(upload_to = 'images/',null=True)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    
    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()