from django.db import models
from django.contrib.auth.models import User
from standard.models import Standard
from school.models import School, ClassRoom


class Teacher(Standard):
  """
    Representa um professor no sistema, com informações pessoais e associações a escolas e salas de aula.

    Esta classe herda de `Standard` e está vinculada a um usuário específico do sistema,
    armazenando informações como CPF e associando o professor a várias escolas e salas de aula.

    Atributos:
        user (models.OneToOneField): Relacionamento de um-para-um com o modelo `User`,
            representando o usuário associado ao professor.
        cpf (models.CharField): CPF do professor. Este campo é obrigatório, deve ter 11 caracteres
            e deve ser único no sistema.
        schools (models.ManyToManyField): Relação de muitos-para-muitos com o modelo `School`,
            permitindo que um professor esteja associado a várias escolas.
        class_rooms (models.ManyToManyField): Relação de muitos-para-muitos com o modelo `ClassRoom`,
            permitindo que um professor esteja associado a várias salas de aula.

    Meta:
        verbose_name (str): Nome legível para a classe no singular.
        verbose_name_plural (str): Nome legível para a classe no plural.

    Métodos:
        __str__(): Retorna o nome completo do professor baseado nos atributos `first_name` e `last_name`
            do usuário associado.
  """
  user = models.ForeignKey(
    User,
    on_delete=models.DO_NOTHING
  )
  cpf = models.CharField(
    'Cpf',
    max_length=11,
    blank=False,
    null=False,
    unique=True
  )
  schools = models.ManyToManyField(
    School,
    related_name='schools_teacher'
  )
  class_rooms = models.ManyToManyField(
    ClassRoom,
    related_name='classrooms_teacher'
  )
  
  class Meta:
    verbose_name = 'Teacher'
    verbose_name_plural = 'Teachers'
  
  def __str__(self):
    return f'{self.user.first_name} {self.user.last_name}'
  
