from django import forms
from .models import Profile,Image,Comment

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