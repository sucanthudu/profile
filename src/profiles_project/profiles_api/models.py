from django.db import models
#models imported
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
#user manager from django imported


class UserProfileManager(BaseUserManager):
    """Helps Django to understand and work with our custom user model"""

    def create_user(self, email, name, password=None):
        """Creates a new super(admin) user profile object"""

        if not email:
             #if email field is blank or none this returns(condition is) True
             raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,) #gets username and email from UserProfile model and assigns it to user obj and therby saving to db

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates a superuser with given details"""

        user = self.create_user(email, name, password)
        #super user settings and save it to db
        user.is_superuser=True
        user.is_staff=True

        user.save(using=self._db)

        return user


# Create your models here.
# UserProfile class created
# inherits base user models and permissions model from django to create our custom user profile model
# UserProfile is the custom model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile"""
#fields

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

#objects manager
    objects = UserProfileManager()

#for logging in these below fields are required.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get users fullname"""

        return self.name

    def get_short_name(self):
        """Used to get users shortname"""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email

class ProfileFeedItem(models.Model):
    """Profile status update"""

    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return the model as string"""

        return self.status_text
