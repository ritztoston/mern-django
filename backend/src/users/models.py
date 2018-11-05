from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

def upload_avatar(instance, filename):
    return "updates/{username}/{filename}".format(username=instance.username, filename=filename)

class UserProfileManager(BaseUserManager):

    def create_user(self, email, username, firstname, lastname, avatar, password):
        #return true if null or false
        if not email:
            raise ValueError('Users must have an email address.')

        if not avatar:
            avatar = 'Descartes_Labs.png'

        email = self.normalize_email(email)

        user = self.model(email=email, firstname=firstname, lastname=lastname, username=username, avatar=avatar)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, firstname, lastname, avatar, password):
        user = self.create_user(email, username, firstname, lastname, avatar, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True, null=True, blank=True, error_messages={'unique': 'This email already exists.'})
    username = models.CharField(max_length=255, unique=True, null=True, blank=True, error_messages={'unique': 'This username already exists.'})
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to=upload_avatar, null=True, blank=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'firstname', 'lastname', 'avatar']

    def get_fullname(self):
        return self.firstname+' '+self.lastname

    def __str__(self):
        return self.username
