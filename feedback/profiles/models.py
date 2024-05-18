from django.db import models
import os 

# Create your models here.

class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")

    def image_name(self):
       img = self.image.name.split('/')
       return img[-1]