from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    issue = models.CharField(max_length=300)
    status = models.BooleanField(default=False)
    reply = models.CharField(max_length=300, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
