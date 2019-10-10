# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


class Actor(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    login = models.CharField(max_length=50, unique=True)
    avatar_url = models.URLField()

    def __str__(self):
        return self.avatar_url


class Repo(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50, help_text="name field")
    url = models.URLField(help_text="url field")

    def __str__(self):
        return self.name


class Event(models.Model):
    """ Model representing a book """
    id = models.IntegerField(unique=True, primary_key=True)
    type = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    actor = models.ForeignKey(Actor, on_delete=models.SET_NULL, null=True, related_name='actors')
    repo = models.ForeignKey(Repo, on_delete=models.SET_NULL, null=True, related_name='repos')

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['id']


