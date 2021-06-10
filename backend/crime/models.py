'''
from common.models import DataTransferObject
from django.db import models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


class CrimeVo(models.Model):
    police = models.TextField()
    crime = models.TextField()
    create_at = models.DateTimeField()


class CrimeDto(DataTransferObject):
    police = ''
    crime = ''
    create_at = ''
'''
