from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from .models import *
from django.db.models import Q

from django.http import JsonResponse
from django.conf import settings
import os

import joblib
import numpy as np

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about/about.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #create a new registration object and avoid saving it yet
            new_user = user_form.save(commit=False)
            #reset the choosen password
            new_user.set_password(user_form.cleaned_data['password'])
            #save the new registration
            new_user.save()
            return render(request, 'registration/register_done.html',{'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html',{'user_form':user_form})

def profile(request):
    return render(request, 'profile/profile.html')



@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user = user_form.save()
            profile = user.profile
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
    else:
        user_form = EditProfileForm(instance=request.user)
    
    return render(request, 'profile/edit_profile.html', {'user_form': user_form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Your account was successfully deleted.')
        return redirect('base')  # Redirect to the homepage or another page after deletion

    return render(request, 'registration/delete_account.html')
# das
@login_required
def dashboard(request):
    users_count = User.objects.all().count()

    context = {
        'users_count':users_count,
    }
    return render(request, "dashboard/dashboard.html", context=context)

# Contact start
@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us!")
            return redirect('dashboard')  # Redirect to the same page to show the modal
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
# contact end
