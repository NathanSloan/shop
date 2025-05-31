from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# class - defines an object
# models.Model - states object is a Django Model, saves to database
class Quote(models.Model):
    # models.ForeignKey - states attribute is a link to another model
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # models.CharField - states attribute is text with a limited number of characters
    title = models.CharField(max_length=200)
    # models.TextField - states attribute is text of an undefined length
    text = models.TextField()
    # models.DateTimeField - states attribute is a field of date/time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # def - defines a method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title