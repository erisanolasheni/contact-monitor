# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BaseModel(models.Model):
    # create a base class for recording create and modified times
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now=True)

# create a child class model that would be used for the Contacts models
class Contact(BaseModel):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True)

    class Meta():
        ordering = ["-pk"]
