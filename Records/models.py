# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from  RecProject import settings


class Records(models.Model):
    '''
    Records
    creates and manipulates a db object
    '''

    name = models.CharField(max_length= 50)
    emailAdd = models.EmailField()

    def getName(self):
        return self.name.__str__()

    def getEmail(self):
        return  self.emailAdd.__str__()

# Create your models here.
