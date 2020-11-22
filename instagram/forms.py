from django import forms
from django.contrib.auth.models import User
from .models import Profile,Image,Comment


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','profile_photo','bio']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','caption']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']