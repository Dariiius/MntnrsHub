"""
Main Ajax
"""
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse

from app_main.models import UserProfile
from app_main.utils import save_session, validate_registration


def post_login(request):
    """
    Ajax login
    """
    success = False
    message = 'An error occured. Please try again later.'
    data = request.POST
    user = authenticate(request, username=data.get('username', ''), password=data.get('password', ''))

    if user is not None:
        logged = save_session(request, user)

        if logged:
            success = True
            message = 'Login Successful!'
    else:
        message = 'Incorrect username or password.'

    response = {
        'success': success,
        'message': message
    }

    return JsonResponse(response)


def post_register(request):
    """
    Ajax register
    """
    success = False
    message = 'An error occured. Please try again later.'
    data = request.POST
    validated = validate_registration(data)

    if validated['success']:
        user = User.objects.create_user(
            data.get('username'),
            data.get('email'),
            data.get('password'),
        )

        user.first_name = data.get('firstname', '').lower()
        user.last_name = data.get('lastname', '').lower()
        user.save()

        if user:
            user_profile = UserProfile.objects.create(
                user=user,
                middle_name=data.get('middlename', '').lower(),
                age=data.get('age', 0),
                gender=data.get('gender', 'male')
            )

            if user_profile:
                success = True
                message = 'Congratulations, your account has been successfully created.'
    else:
        message = validated['errors'][0]

    response = {
        'success': success,
        'message': message
    }

    return JsonResponse(response)
