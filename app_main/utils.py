"""
Main Utils
"""
from django.contrib.auth.models import User

from app_main.models import UserProfile


def save_session(request, user):
    user_profile = UserProfile.objects.get(user=user)

    request.session['user'] = {
        'user_id': user.id,
        'email_address': user.email,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'middle_name': user_profile.middle_name,
        'age': user_profile.age,
        'gender': user_profile.gender,
    }

    return True


def validate_registration(data):
    success = True
    errors = []

    email = User.objects.filter(email=data.get('email'))
    username = User.objects.filter(username=data.get('username'))

    if data.get('username', '') == '':
        errors.append('Username is required.')
        success = False

    if len(username) > 0:
        errors.append('Username is already taken.')
        success = False

    if data.get('password', '') == '':
        errors.append('Password is required.')
        success = False

    if data.get('password') != data.get('password_confirm'):
        errors.append('Passwords don\'t match.')
        success = False

    if data.get('email', '') == '':
        errors.append('Email address is required.')
        success = False

    if len(email) > 0:
        errors.append('Email address is already registered.')
        success = False

    if data.get('firstname', '') == '':
        errors.append('First name is required.')
        success = False

    if data.get('lastname', '') == '':
        errors.append('Last name is required.')
        success = False

    if data.get('age', '') == '':
        errors.append('Age is required.')
        success = False

    return {
        'success': success,
        'errors': errors
    }
