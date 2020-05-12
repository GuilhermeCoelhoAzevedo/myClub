from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField(
        'Venue name',
        max_length=120
    )

    address = models.CharField(
        max_length=300
    )

    zip_code = models.CharField(
        'Zip/Postal Code',
        max_length=12
    )

    phone = models.CharField(
        'Contact Phone',
        max_length=20,
        blank=True
    )

    web = models.URLField(
        'Web Address',
        blank=True
    )

    email_address = models.EmailField(
        'Email address',
        blank=True
    )

    def __str__(self):
        return self.name


class MyclubUser(models.Model):
    first_name = models.CharField(
        max_length=30
    )

    last_name = models.CharField(
        max_length=30
    )

    email = models.EmailField(
        'User email'
    )

    def __str__(self):
        return self.first_name + " " + self.last_name


class Event(models.Model):

    name = models.CharField(
        'Event name',
        max_length=120
    )

    event_date = models.DateTimeField(
        'Event Date'
    )

    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE
    )

    manager = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    attendees = models.ManyToManyField(
        MyclubUser
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name