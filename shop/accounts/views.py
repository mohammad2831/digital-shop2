from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm,  UserLoginForm
from . models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import send_email_via_sender_net
from orders.models import Order

class UserRegisterView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    form_class = UserRegistrationForm
    def get(self, request):
        
        form = self.form_class
        return render(request, 'accounts/register.html', {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['email'], cd['phone'], cd['full_name'], cd['password'])
            subject = 'Welcome to Our Site!'
            content = 'Thank you for signing up for our site. We hope you enjoy your stay.'
          #  send_welcome_email(cd['email'], subject, content)
            messages.success(request, 'you registered succesfuli', 'success')
            return redirect('home:home')
        return render(request,'accounts/register.html', {'form':form})



class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logout succes ', 'success')
        return redirect('home:home')
    
    

class UserLoginView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    form_class = UserLoginForm

    def get(self, request):
        
        form = self.form_class()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in successfully', 'success')
                return redirect('home:home')
            
            messages.error(request, 'Email or password is wrong', 'danger')

        return render(request, 'accounts/login.html', {'form': form})
    



class UserProfile(View):
    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user=user)
        return render(request, 'accounts/profile.html', {'user': user, 'orders': orders})
    
class ProfileOrderDetail(View):
    def get(self, request):
        pass












def send_test_email(request):
    to_email = 'mhmd.2831.mahdi@gmail.com'
    subject = 'آزمایش ارسال ایمیل'
    message = '<h1این یک ایمیل تست از Django است که با استفاده از Sender.net ارسال شده است.</h1>'
    
    send_email_via_sender_net(to_email, subject, message)
    
    return HttpResponse('ایمیل ارسال شد!')