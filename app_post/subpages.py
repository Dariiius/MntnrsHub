"""
Post Subpages
"""
from django.shortcuts import render

from app_post.models import Post


def post_list(request):
    """
    Post list subpage
    """
    context = dict()
    template = 'app_post/subpages/post_list.html'
    post_array = []

    posts = Post.objects.filter(
        status='posted'
    ).order_by('-pk')

    for post in posts:
        if post.visibility_status == 'private' and post.user.id != request.session['user']['user_id']:
            continue

        post_array.append({
            'id': post.id,
            'creator': {
                'user_id': post.user.id,
                'first_name': post.user.first_name,
                'last_name': post.user.last_name,
            },
            'content': post.content,
            'date_posted': post.date_posted,
            'status': post.status,
            'visibility_status': post.visibility_status
        })

    context['posts'] = post_array

    return render(request, template, context)


def post_details(request):
    """
    Post details subpage
    """
    context = dict()
    template = 'app_post/subpages/edit_post.html'
    data = request.GET

    post = Post.objects.get(id=data.get('id'))

    context['post'] = {
        'id': post.id,
        'content': post.content,
        'visibility_status': post.visibility_status
    }

    return render(request, template, context)
