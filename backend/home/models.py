from django.conf import settings
from django.db import models


class Customer(models.Model):
    "Generated Model"
    firstname = models.CharField(
        max_length=256,
    )
    lastname = models.CharField(
        max_length=256,
    )
    email = models.EmailField(
        max_length=254,
    )
    password = models.CharField(
        max_length=256,
    )


class UserProfile(models.Model):
    "Generated Model"
    userid = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="userprofile_userid",
    )
    profile_picture = models.CharField(
        null=True,
        blank=True,
        max_length=700,
    )
