from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Image

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username='Abigail')
        self.user.save()
        self.new_profile = Profile(id=1, name='image', profile_photo='image.jpg', bio='Enjoy Life',
                                    user=self.user)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_image(self):
        self.new_profile.delete_profile()
        users = Profile.objects.all()
        self.assertTrue(len(users) < 1)

class ImageTestClass(TestCase):
    def setUp(self):
        self.new_profile = Profile(name='Abigail', user=User(username='Nelly'))
        
        self.new_image = Image(image='image.png', image_name='image', caption='Enjoy Life', user=self.new_profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image(self):
        self.new_image.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)
        
    
