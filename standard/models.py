from django.db import models

# Create your models here.
from django.db import models
import uuid


class UuidModel(models.Model):
  id = models.UUIDField(
    primary_key=True,
    unique=True,
    default=uuid.uuid4
  )
  
  class Meta:
    abstract = True


class TimeStamped(models.Model):
  created_at = models.DateTimeField(
    auto_now_add=True
  )
  modified_at = models.DateTimeField(
    auto_now_add=True
  )
  
  class Meta:
    abstract = True


class Active(models.Model):
  is_active = models.BooleanField(
    default=True
  )
  
  class Meta:
    abstract = True


class Standard(UuidModel, TimeStamped, Active):

  class Meta:
    abstract = True
