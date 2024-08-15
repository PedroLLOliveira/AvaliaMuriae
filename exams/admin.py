from django.contrib import admin
from .models import (
  QuestionTest,
  TestAnswerSheet,
  SchoolTest
)


@admin.register(QuestionTest)
class QuestionAdmin(admin.ModelAdmin):
  list_display = [
    'hexadecimal',
    'pedagogical_observation',
    'alternative'
  ]


@admin.register(TestAnswerSheet)
class TestAnswerSheetAdmin(admin.ModelAdmin):
  list_display = [
    'rooms',
    'school_supplies'
  ]


@admin.register(SchoolTest)
class SchoolTestAdmin(admin.ModelAdmin):
  list_display = [
    'student',
    'school_supplies',
    'score'
  ]