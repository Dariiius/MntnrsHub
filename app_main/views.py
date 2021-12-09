"""
Main View
"""
from django.shortcuts import render, redirect

from app_main.decorators import require_logged, require_not_logged


@require_logged
def home(request):
    """
    Home page
    """
    context = dict()
    template = 'app_main/home.html'
    context['page'] = {
        'title': 'Home',
    }

    return render(request, template, context)


@require_not_logged
def login(request):
    """
    Login page
    """
    context = dict()
    template = 'app_main/login.html'
    context['page'] = {
        'title': 'Login',
    }

    return render(request, template, context)


def logout(request):
    """
    Login page
    """
    context = dict()
    try:
        request.session.flush()
    except Exception as e:
        print(e)

    context['page'] = {
        'title': 'Logout',
    }

    return redirect('app_main:login')


@require_not_logged
def registration(request):
    """
    Registration page
    """
    context = dict()
    template = 'app_main/registration.html'
    context['page'] = {
        'title': 'Registration',
    }

    return render(request, template, context)
