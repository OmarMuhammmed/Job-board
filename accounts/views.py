from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth import login
from django.urls import reverse
from django.shortcuts import redirect   
from .forms import SingupForm, EditUser, EditProfile
from .models import Profile       
# Create your views here.

def signup(request) :
    if request.method =='POST' :
        form = SingupForm(request.POST)
        
        if form.is_valid() :
            # myform = form.save(commit=False)
            form.save()   
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password ) # check in DB if user is exist
            login(request, user)
            return redirect(reverse('accounts:profile'))
    else :
        form = SingupForm()
    
    return render(request,'registration/signup.html', {'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)  # get user who login  
    return render(request, 'accounts/profile.html',{'profile':profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user) # get user who login 

    if request.method =="POST" :
        edituser = EditUser(request.POST,instance=request.user)
        editprofile = EditProfile(request.POST,request.FILES,instance = profile )
        if edituser.is_valid() and editprofile.is_valid():
           edituser.save()
           myprofie= editprofile.save(commit=False)
           myprofie.user = request.user
           myprofie.save()
           return redirect(reverse('accounts:profile'))
        
    
    else :
        edituser = EditUser(instance=request.user)
        editprofile = EditProfile(instance= profile)
        


    return render(request, 'accounts/profile_edit.html',{'edituser':edituser, 'editprofile':editprofile})
    

