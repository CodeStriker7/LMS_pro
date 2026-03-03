from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Foydalanuvchi rollarini yaratamiz
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    
    # Qo'shimcha ma'lumotlar
    phone = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.username