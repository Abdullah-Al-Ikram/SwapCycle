from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, SellerRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
def signup_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'User account created!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'back/signup.html', {'form': form})

def signup_seller(request):
    if request.method == 'POST':
        form = SellerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Seller account created!')
            return redirect('home')
    else:
        form = SellerRegisterForm()
    return render(request, 'back/signup-seller.html', {'form': form})

def redirect_user_by_role(user):
    return redirect('dashboard')

def signin(request):
    if request.method == 'POST':
        signin_form = AuthenticationForm(request=request, data=request.POST)
        if signin_form.is_valid():
            username = signin_form.cleaned_data['username']
            password = signin_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('home')
                #return redirect_user_by_role(user)
            else:
                messages.error(request, "Invalid username or password.")
    else:
        signin_form = AuthenticationForm()
    return render(request, 'back/signin.html', {'signin_form': signin_form})

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'back/profile.html', {'user': user})


@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'back/update_profile.html', {'form': form})

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('signin')