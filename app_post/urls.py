"""
Post URLs
"""
from django.urls import path

from app_post import ajax, subpages

app_name = 'app_post'

urlpatterns = [
    path('post/post/', ajax.post_post, name='post_post'),
    path('edit/post/', ajax.edit_post, name='edit_post'),
    path('delete/post/', ajax.delete_post, name='delete_post'),
    path('subpage/post/list/', subpages.post_list, name='post_list'),
    path('subpage/post/details/', subpages.post_details, name='post_details'),
]
