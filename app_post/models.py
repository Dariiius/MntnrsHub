"""
Post Models
"""
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    """
    Post Model
    """
    POST_STATUS = (
        ('posted', 'Posted'),
        ('archived', 'Archived')
    )
    VISIBILITY_STATUS = (
        ('public', 'Public'),
        ('private', 'Private')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(default='', max_length=255, blank=True, null=True)
    date_posted = models.DateTimeField(default=now)
    status = models.CharField(max_length=50, choices=POST_STATUS, default=POST_STATUS[0][0])
    visibility_status = models.CharField(max_length=50, choices=VISIBILITY_STATUS, default=VISIBILITY_STATUS[0][0])
