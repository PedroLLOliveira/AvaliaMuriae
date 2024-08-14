from django.db import models
from standard.models import Standard
from school.models import School, ClassRoom


class Student(Standard):
  first_name = models.CharField(
    'Primeiro nome',
    max_length=150,
    blank=False,
    null=False
  )
  last_name = models.CharField(
    'Ultimo nome',
    max_length=150,
    blank=False,
    null=False
  )
  inep = models.CharField(
    'INEP',
    max_length=12,
    blank=False,
    null=False,
    unique=True
  )
  school = models.ForeignKey(
    School,
    on_delete=models.DO_NOTHING
  )
  class_room = models.ForeignKey(
    ClassRoom,
    on_delete=models.DO_NOTHING
  )
  
  class Meta:
    ordering = ('first_name', 'last_name')
    verbose_name = 'Student'
    verbose_name_plural = 'Students'
    
  def __str__(self):
    return f'{self.first_name} {self.last_name}'
