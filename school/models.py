from django.db import models
from standard.models import Standard


class School(Standard):
  """
    Representa uma escola no sistema, com informações básicas como nome e censo.

    Esta classe herda de `Standard` e inclui atributos para armazenar o nome
    da escola e um identificador único de censo.

    Atributos:
        name (models.CharField): Nome da escola. Este campo é obrigatório e possui
            um limite máximo de 256 caracteres.
        census (models.CharField): Código de censo único da escola. Este campo é
            obrigatório, possui um limite máximo de 10 caracteres e deve ser único.

    Meta:
        ordering (tuple): Define a ordenação padrão por nome.
        verbose_name (str): Nome legível para a classe no singular.
        verbose_name_plural (str): Nome legível para a classe no plural.

    Métodos:
        __str__(): Retorna o nome da escola.
  """
  name = models.CharField(
    'Nome',
    max_length=256,
    blank=False,
    null=False
  )
  census = models.CharField(
    'Censo',
    max_length=10,
    blank=False,
    null=False,
    unique=True
  )
  
  class Meta:
    ordering = ('name', )
    verbose_name = 'School'
    verbose_name_plural = 'Schools'
  
  def __str__(self):
    return f'{self.name}'


class ClassRoom(Standard):
  """
    Representa uma sala de aula em uma escola, incluindo informações sobre o ano,
    nome da turma e código da turma.

    Esta classe herda de `Standard` e associa uma sala de aula a uma escola específica,
    além de fornecer atributos para o nome da turma, o ano e o código da turma.

    Atributos:
        school (models.ForeignKey): Chave estrangeira que relaciona a sala de aula a uma escola.
        room (models.CharField): Nome da turma. Este campo é obrigatório e possui
            um limite máximo de 1 caractere.
        year (models.CharField): Ano em que a turma está registrada. Este campo é obrigatório
            e possui um limite máximo de 10 caracteres.
        cod_classroom (models.CharField): Código da turma. Este campo é obrigatório e possui
            um limite máximo de 10 caracteres.

    Meta:
        ordering (tuple): Define a ordenação padrão primeiro pelo nome da turma e depois pelo ano.
        verbose_name (str): Nome legível para a classe no singular.

    Métodos:
        __str__(): Retorna uma string representando a sala de aula no formato 'ano - turma'.
  """
  school = models.ForeignKey(
    School,
    on_delete=models.DO_NOTHING
  )
  room = models.CharField(
    'Nome da Turma',
    max_length=1,
    blank=False,
    null=False
  )
  year = models.CharField(
    'Ano',
    max_length=10,
    blank=False,
    null=False
  )
  cod_classroom = models.CharField(
    'Codigo da turma',
    max_length=10,
    blank=False,
    null=False
  )
  
  class Meta:
    ordering = ('room', 'year')
    verbose_name = 'ClassRoom'
  
  def __str__(self):
    return f'{self.year} - {self.room}'
