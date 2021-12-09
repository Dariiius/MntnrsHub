"""
Main Models
"""

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """
    User Profile Model
    """
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(default='', max_length=255, blank=True, null=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=50, choices=GENDER, default=GENDER[0][0])

