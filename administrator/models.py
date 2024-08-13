from django.db import models
from standard.models import Standard
from django.contrib.auth.models import User


class Administrator(Standard):
  """
    Representa um administrador no sistema.

    Esta classe herda de `Standard` e estende suas funcionalidades para armazenar
    informações adicionais de um administrador, como o setor de atuação e CPF.

    Atributos:
        user (models.OneToOneField): Relacionamento um-para-um com a tabela de usuários,
            referenciando o usuário ao qual o administrador está vinculado.
        sector (models.CharField): Campo opcional que indica o setor de atuação do administrador.
            As opções disponíveis são 'M' (Masculino).
        cpf (models.CharField): Campo obrigatório que armazena o CPF (Cadastro de Pessoa Física) do administrador.

    Métodos:
        __str__(): Retorna o nome completo do administrador, combinando o primeiro
            e o último nome do usuário vinculado.
  """
  user = models.OneToOneField(
      User,
      on_delete=models.DO_NOTHING
  )
  sector = models.CharField(
    'Setor',
    max_length=30,
    choices=[('PROJETOS E INOVACAO', 'Projetos e Inovação'),],
    null=True,
    blank=True
  )
  cpf = models.CharField(
    'Cpf',
    max_length=11,
    null=False,
    blank=False
  )

  class Meta:
    verbose_name = 'Administrator'
    verbose_name_plural = 'Administrators'
  
  def __str__(self):
    return f'{self.user.first_name} {self.user.last_name}'
