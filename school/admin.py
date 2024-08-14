from django.contrib import admin
from .models import School, ClassRoom


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
  list_display = [
    'name',
    'census'
  ]


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
  list_display = [
    'school',
    'room',
    'year',
    'cod_classroom'
  ]
