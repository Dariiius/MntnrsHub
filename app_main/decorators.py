"""
Main Decorators
"""
from django.shortcuts import redirect


def require_logged(view_func):
    def wrapper_func(request, *args, **kwargs):
        if 'user' not in request.session:
            return redirect('app_main:login')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def require_not_logged(view_func):
    def wrapper_func(request, *args, **kwargs):
        if 'user' in request.session:
            return redirect('app_main:home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
