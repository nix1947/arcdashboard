from django.shortcuts import render


def dashboard(request):
    """serve as a dashboard"""
    return render(request, 'dashboard/dashboard.html', {})
