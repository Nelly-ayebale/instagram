from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Profile,Image,Comment
from django.contrib.auth.models import User
from .forms import ProfileForm,ImageForm,CommentForm,UserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts/login/')
def home(request):
    users = User.objects.exclude(id=request.user.id)
    images = Image.images()
    
    if request.method == 'POST':
       
        form = ImageForm(request.POST,request.FILES)
       
        
        
        if form.is_valid() :
            image = form.save(commit=False)
            image.profile = request.user.profile
            image.save()
        
            
            return redirect('home')
    else:
        
        form = ImageForm()
    return render(request,'instagrams/home.html',{"users":users,"images":images,"form":form})

@login_required(login_url='accounts/login/')
def profile(request,username):
    images = request.user.profile.images.all()
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            return redirect('home')
        
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'instagrams/profile.html', {'user_form': user_form,'profile_form': profile_form,"images":images})

@login_required(login_url='accounts/login/')
def user(request,username):
    user_form = get_object_or_404(User, username=username)
    

    if request.user == user_form:
        return redirect('profile', username=request.user.username)
    images = user_form.profile.images.all()
    
    
    
    return render(request,'instagrams/user.html',{"user_form":user_form,"images":images})
    
@login_required(login_url='accounts/login/')
def search_by_profile(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_profile(search_term)
        message = f"{search_term}"

        return render(request, 'instagrams/search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'instagrams/search.html',{"message":message})
