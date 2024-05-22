from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    place=models.TextField()
    phone=models.IntegerField(default=0)
    is_principle=models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
def __str__(self):
    return self.username