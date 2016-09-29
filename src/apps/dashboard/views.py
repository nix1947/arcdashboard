from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.urls import reverse


def login(request):
    """Login page"""
    # If user is already login redirect user to dashboard
    if request.user.is_authenticated():
        # Redirect user to dashboard
        return HttpResponseRedirect(reverse('dashboard'))

    if request.method == "POST":
        # Get the username and password from the form
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            # check whether the user is active or not
            if user.is_active:
                auth_login(request, user) # Login the user
                # Redirect user to  dashboard
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                # User is not active
                # Render the login page with error message
                error = "Your account is disabled."
                return render(request, 'pages/login.html', {'error': error})
        else:
            # Render the login page with error message
            error = "Invalid username or password"
            return render(request, 'pages/login.html', {'error':error})
    else:
        # Display the form for GET request
        return render(request, 'pages/login.html')

@login_required(redirect_field_name="dashboard")
def dashboard(request):
    """serve as a dashboard"""
    return render(request, 'dashboard/dashboard.html', {})

@login_required(redirect_field_name="/")
def logout(request):
    """View that logout the user session """
    auth_logout(request) # Logout the user
    # Redirect to Login page
    return HttpResponseRedirect(reverse('login'))
