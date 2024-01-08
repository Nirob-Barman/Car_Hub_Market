from typing import Any
from django.forms.forms import BaseForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from cars.models import Car
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib import messages


from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DetailView, DetailView
from django.views import View

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


def profile(request):
    if request.user.is_authenticated:
        bought_cars = Car.objects.filter(buyers=request.user)
        # print(bought_cars)
        # for car in bought_cars:
        #     print(car.quantity)

        return render(request, 'profile.html', {'bought_cars': bought_cars})
    else:
        return redirect('login')


def privacy_settings(request):
    if request.user.is_authenticated:
        return render(request, 'profile_settings.html', {'title': 'Privacy Settings', 'user': request.user})
    else:
        return redirect('login')


def signup(request):
    if not request.user.is_authenticated:
        form = forms.RegisterForm()
        if request.method == 'POST':
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save()
                return redirect('login')
                # return redirect('home')
                # return redirect('profile')

        else:
            form = forms.RegisterForm()
        return render(request, 'form.html', {'form': form, 'title': 'Sign Up', 'button_text': 'Sign Up', 'button_class': 'btn-success'})
    else:
        return redirect('home')
        # return redirect('profile')


class UserSignUpView(SuccessMessageMixin, CreateView):
    form_class = forms.RegisterForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')
    success_message = "Account created successfully"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sign Up'
        context['button_text'] = 'Sign Up'
        context['button_class'] = 'btn-success'
        return context


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            # form = AuthenticationForm(data=request.POST)
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully')
                    messages.info(
                        request, f"You are now logged in as {username}")
                    # return redirect('home')
                    return redirect('privacy_settings')
                else:
                    messages.error(request, 'Invalid username or password')

        else:
            form = AuthenticationForm()
        return render(request, 'form.html', {'form': form, 'title': 'Login', 'button_text': 'Login', 'button_class': 'btn-primary'})
    else:
        return redirect('home')
        # return redirect('profile')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'form.html'

    def get_success_url(self):
        return reverse_lazy('privacy_settings')

    def form_valid(self, form):
        messages.success(self.request, 'Logged In Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['button_text'] = 'Login'
        context['button_class'] = 'btn-primary'
        return context


def user_logout(request):
    logout(request)
    messages.info(request, "Logged Out Successfully")
    return redirect('home')


# class UserLogoutView(LogoutView):
#     next_page = 'home'

#     def dispatch(self, request, *args, **kwargs):
#         response = super().dispatch(request, *args, **kwargs)
#         messages.info(self.request, "Logged Out Successfully")
#         return response

class UserLogoutView(View):

    def get(self, request):
        logout(request)
        messages.info(request, "Logged Out Successfully")
        return redirect('home')


def password_change(request):
    if request.user.is_authenticated:
        form = PasswordChangeForm(request.user)
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(
                    request, 'Your password was successfully updated!')
                # return redirect('home')
                # return redirect('profile')
                return redirect('privacy_settings')
            else:
                messages.error(request, 'Please correct the error below.')
        return render(request, 'form.html', {'form': form, 'title': 'Change Your Password', 'button_text': 'Change Password', 'button_class': 'btn-warning'})
    else:
        return redirect('home')
        # return redirect('profile')


def password_change_without_old_password(request):
    if request.user.is_authenticated:
        form = SetPasswordForm(request.user)
        if request.method == 'POST':
            form = SetPasswordForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(
                    request, 'Your password was successfully updated!')
                # return redirect('home')
                # return redirect('profile')
                return redirect('privacy_settings')
            else:
                messages.error(request, 'Please correct the error below.')
        return render(request, 'form.html', {'form': form, 'title': 'Change Your Password without Old Password', 'button_text': 'Change Password', 'button_class': 'btn-danger'})
    else:
        return redirect('home')
        # return redirect('profile')


def edit_privacy_settings(request):
    if request.user.is_authenticated:
        form = forms.EditProfileForm(instance=request.user)
        if request.method == 'POST':
            form = forms.EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(
                    request, 'Your user data was successfully updated.')
                form.save()
                # return redirect('home')
                # return redirect('profile')
                return redirect('privacy_settings')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = forms.EditProfileForm(instance=request.user)
        return render(request, 'form.html', {'form': form, 'title': 'Edit Your Profile', 'button_text': 'Update Profile', 'button_class': 'btn-info'})
    else:
        return redirect('home')
        # return redirect('profile')
