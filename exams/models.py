from django.db import models
from standard.models import Standard
from student.models import Student


class Question(Standard):
    hexadecimal = models.CharField(
      'Hexadecimal',
      max_length=16,
      blank=False,
      null=False
    )
    pedagogical_observation = models.TextField()
    alternative = models.CharField(
      'Alternative',
      max_length=1,
      choices=[('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'), ('E', 'e')]
    )
    
    class Meta:
      verbose_name = 'Question'
      verbose_name_plural = 'Questions'

    def __str__(self):
      return f'{self.hexadecimal} - {self.pedagogical_observation}'


class TestAnswerSheet(Standard):
  correct_answer = models.ManyToManyField(
    Question,
    related_name='questions_test_answer_sheet'
  )
  rooms = models.CharField(
    'Turmas',
    max_length = 10,
    choices=[('1° AO 5°', '1° ao 5°'), ('6°', '6°'), ('7°', '7°'), ('8°', '8°'), ('9°', '9°')],
    blank=False,
    null=False
  )
  school_supplies = models.CharField(
    'Materia escolar',
    max_length = 50,
    choices=[
      ('PORTUGUES', 'Português'),
      ('MATEMATICA', 'Matemática')
    ]
  )
  
  class Meta:
    verbose_name = 'Test Answer Sheet'
    verbose_name_plural = 'Tests Answer Sheet'


class SchoolTest(Standard):
  student = models.ForeignKey(
    Student,
    on_delete=models.DO_NOTHING
  )
  school_supplies = models.CharField(
    'Materia escolar',
    max_length = 50,
    choices=[
      ('PORTUGUES', 'Português'),
      ('MATEMATICA', 'Matemática')
    ]
  )
  student_response = models.ManyToManyField(
    Question,
    related_name='school_test_question'
  )
  score = models.PositiveIntegerField(
    blank=True,
    null=True
  )
  
  class Meta:
    verbose_name = 'School test'
    verbose_name_plural = 'School tests'
  
  