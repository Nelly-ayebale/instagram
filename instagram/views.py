from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Profile,Image,Comment
from django.contrib.auth.models import User
from .forms import ProfileForm,ImageForm,CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts/login/')
def home(request):
    users = User.objects.exclude(id=request.user.id)
    images = Image.images()

    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user.profile 
            image.save_image()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request,'instagrams/home.html',{"users":users,"images":images,"form":form})

    