from django.db import models
from standard.models import Standard
from student.models import Student


class QuestionTest(Standard):
    """
    Representa uma questão em um exame, incluindo sua representação hexadecimal, 
    uma observação pedagógica e a alternativa correta.

    Atributos:
        hexadecimal (str): Código hexadecimal que identifica unicamente a questão.
        pedagogical_observation (str): Observação pedagógica associada à questão.
        alternative (str): Alternativa correta para a questão. Pode ser uma das opções: 'A', 'B', 'C', 'D', ou 'E'.

    Meta:
        verbose_name (str): Nome singular para a classe no admin do Django.
        verbose_name_plural (str): Nome plural para a classe no admin do Django.

    Métodos:
        __str__(): Retorna uma string representando a questão, composta pelo código hexadecimal e pela observação pedagógica.
    """
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
    """
    Representa um gabarito de um teste escolar, incluindo as respostas corretas, 
    turmas e matérias escolares associadas.

    Atributos:
        correct_answer (ManyToManyField): Relação com as questões que compõem o gabarito.
        rooms (str): As turmas associadas ao gabarito. Pode ser '1° AO 5°', '6°', '7°', '8°', ou '9°'.
        school_supplies (str): Matéria escolar correspondente ao gabarito. Pode ser 'PORTUGUES' ou 'MATEMATICA'.

    Meta:
        verbose_name (str): Nome singular para a classe no admin do Django.
        verbose_name_plural (str): Nome plural para a classe no admin do Django.
    """
    correct_answer = models.ManyToManyField(
      QuestionTest,
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


class StudentResponse(Standard):
  """
    Representa a resposta de um aluno a uma questão em um teste escolar.

    Atributos:
        question_reference (ForeignKey): Referência à questão que o aluno respondeu.
        response (str): Resposta dada pelo aluno. Pode ser uma das opções: 'A', 'B', 'C', 'D', ou 'E'.

    Meta:
        verbose_name (str): Nome singular para a classe no admin do Django.
        verbose_name_plural (str): Nome plural para a classe no admin do Django.
  """
  question_reference = models.ForeignKey(
    QuestionTest,
    on_delete=models.DO_NOTHING
  )
  response = models.CharField(
    'Response',
    max_length=1,
    choices=[('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'), ('E', 'e')]
  )
  
  class Meta:
    verbose_name = 'Student Response'
    verbose_name_plural = 'Student Responses'
  

class SchoolTest(Standard):
    """
    Representa um teste escolar realizado por um aluno, incluindo suas respostas e pontuação.

    Atributos:
        student (ForeignKey): Referência ao aluno que realizou o teste.
        school_supplies (str): Matéria escolar associada ao teste. Pode ser 'PORTUGUES' ou 'MATEMATICA'.
        student_response (ManyToManyField): Relação com as respostas do aluno para as questões do teste.
        score (int): Pontuação obtida pelo aluno no teste.

    Meta:
        verbose_name (str): Nome singular para a classe no admin do Django.
        verbose_name_plural (str): Nome plural para a classe no admin do Django.
    """
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
      StudentResponse,
      related_name='school_test_student_response'
    )
    score = models.PositiveIntegerField(
      blank=True,
      null=True
    )
    
    class Meta:
      verbose_name = 'School test'
      verbose_name_plural = 'School tests'
  
  