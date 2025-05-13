from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.username} ({self.role})"

    def save(self, *args, **kwargs):
        if not self.role:
            self.role = 'user'
        super().save(*args, **kwargs)

