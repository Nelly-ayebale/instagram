from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=60,null=True,blank=True)
    profile_photo = CloudinaryField('image')
    bio = HTMLField()

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=100,blank=True,null=True)
    caption = models.CharField(max_length=300,null=True,blank=True)
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

class Comment(models.Model):
    comment_owner = models.ForeignKey('Profile',on_delete=models.CASCADE)
    image_commented = models.ForeignKey('Image',on_delete=models.CASCADE)
    comment = models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.comment
