from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Image

# Create your tests here.
class ProfileTestClass(TestCase.):
    def setUp