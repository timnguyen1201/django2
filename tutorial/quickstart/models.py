from django.utils import timezone

from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    description = models.TextField("description", max_length=150, blank=True)
    location = models.TextField("location", max_length=40, blank=True)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="not sure"),
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)
