# -*- coding: utf-8
from django.db import models


class User(models.Model):

    username = models.CharField()
    password = models.CharField()