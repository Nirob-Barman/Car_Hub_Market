from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from cars.models import Car
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib import messages
# Create your views here.


def profile(request):
    if request.user.is_authenticated:
        bought_cars = Car.objects.filter(buyers=request.user)
        print(bought_cars)
        for car in bought_cars:
            print(car.quantity)

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
            form = AuthenticationForm()
        return render(request, 'form.html', {'form': form, 'title': 'Login', 'button_text': 'Login', 'button_class': 'btn-primary'})
    else:
        return redirect('home')
        # return redirect('profile')


def user_logout(request):
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
