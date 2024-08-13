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
