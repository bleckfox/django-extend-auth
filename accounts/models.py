from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    pass
    # can add fields here, but don't know how
    def __str__(self):
        return self.email