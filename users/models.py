from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


# setup custom user
class CustomUser(AbstractUser):
    object = CustomUserManager()
