from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .forms import SignupForm,LoginForm
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import non_authenticated
# Create your views here.

@non_authenticated
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user=auth.authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password1'))
            if user is not None:
                auth.login(request,user)
            return HttpResponseRedirect(reverse("acc_profile"))
    else:
        form=SignupForm()
    return render(request,'acc/signup.html',{'form':form})

@non_authenticated
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=auth.authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
            if user is not None:
                auth.login(request,user)
                print("login")
                return HttpResponseRedirect(reverse("acc_profile"))
            else:
                messages.info(request,"Invalid password")
                return HttpResponseRedirect(reverse('acc_login'))
    else:
        form=LoginForm()
    return render(request,'acc/login.html',{'form':form})

@login_required(login_url='acc_login')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('acc_signup'))

@login_required(login_url='acc_login')
def profile(request):
    return render(request,'acc/profile.html')

@login_required(login_url='acc_login')
def delete(request):
    if request.method=='POST':
        user=User.objects.get(pk=request.user.id)
        user.delete()
        return HttpResponseRedirect(reverse('acc_signup'))
    return render(request,'acc/delete_account.html')

@login_required(login_url='acc_login')
def user_upload(request):
    upload=request.user.upload.all()
    return render(request,'main/upload/user_upload.html',{'upload':upload})



