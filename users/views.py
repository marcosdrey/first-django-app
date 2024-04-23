from django.shortcuts import render, redirect
from .forms import RegisterUser, UpdateUser, UpdateProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created! Welcome, {username}!')
            return redirect('login')
    else:
        form = RegisterUser()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        upuser_form = UpdateUser(request.POST, instance=request.user)
        upprofile_form = UpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        if upuser_form.is_valid() and upprofile_form.is_valid():
            upuser_form.save()
            upprofile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        upuser_form = UpdateUser(instance=request.user)
        upprofile_form = UpdateProfile(instance=request.user.profile)
    context = {
        'upuser_form': upuser_form,
        'upprofile_form': upprofile_form,
    }

    return render(request, 'users/profile.html', context)