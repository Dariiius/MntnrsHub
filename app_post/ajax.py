"""
Post Ajax
"""
from django.contrib.auth.models import User
from django.http import JsonResponse

from app_main.decorators import require_logged
from app_post.models import Post


@require_logged
def post_post(request):
    """
    Ajax post create
    """
    success = False
    message = 'An error occured. Please try again later.'
    data = request.POST

    user = User.objects.get(id=request.session['user']['user_id'])
    post = Post.objects.create(
        user=user,
        content=data.get('new_post', ''),
        visibility_status=data.get('visibility'),
    )

    if post:
        success = True
        message = 'Post has been published successfully.'

    response = {
        'success': success,
        'message': message
    }

    return JsonResponse(response)


@require_logged
def edit_post(request):
    """
    Ajax post edit
    """
    success = False
    message = 'An error occured. Please try again later.'
    data = request.POST

    post = Post.objects.get(id=data.get('post_id'))

    if post:
        if post.user.id == request.session['user']['user_id']:
            post.content = data.get('post_content', '')
            post.visibility_status = data.get('visibility')
            post.save()

            success = True
            message = 'Post has been updated successfully.'
        else:
            message = 'You don\'t have the permission to do this action.'
    else:
        message = 'Post does not exist.'

    response = {
        'success': success,
        'message': message
    }

    return JsonResponse(response)


@require_logged
def delete_post(request):
    """
    Ajax post delete
    """
    success = False
    message = 'An error occured. Please try again later.'
    data = request.POST

    post = Post.objects.get(id=data.get('post_id'))

    if post:
        if post.user.id == request.session['user']['user_id']:
            post.delete()
            success = True
            message = 'Post has been deleted successfully.'
        else:
            message = 'You don\'t have the permission to do this action.'
    else:
        message = 'Post does not exist.'

    response = {
        'success': success,
        'message': message
    }

    return JsonResponse(response)
