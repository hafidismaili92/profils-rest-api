from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name for user"""
        return self.name
    
    def get_short_name(self):
        """retrieve short name for user"""
        return self.name
    
    def __str__(self):
        """retrieve string representation of our user"""
        return self.email