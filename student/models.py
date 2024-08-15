from django.db import models
from standard.models import Standard
from school.models import School, ClassRoom


class Student(Standard):
    """
    Representa um estudante matriculado em uma escola e associado a uma sala de aula específica.

    A classe `Student` herda de `Standard` e define atributos para armazenar as informações
    básicas do aluno, como nome, sobrenome, e INEP (Identificador Nacional de Estudante).
    Cada estudante está associado a uma escola e a uma sala de aula específicas.

    Atributos:
        first_name (CharField): O primeiro nome do estudante. Este campo é obrigatório.
        last_name (CharField): O último nome do estudante. Este campo é obrigatório.
        inep (CharField): Código INEP único que identifica o estudante. Este campo é obrigatório e único.
        school (ForeignKey): Relação com a escola (`School`) em que o estudante está matriculado.
        class_room (ForeignKey): Relação com a sala de aula (`ClassRoom`) em que o estudante está alocado.

    Meta:
        ordering (tuple): Define a ordenação padrão dos estudantes por primeiro nome e último nome.
        verbose_name (str): Nome singular para exibição no Django Admin.
        verbose_name_plural (str): Nome plural para exibição no Django Admin.

    Métodos:
        __str__(): Retorna uma representação em string do nome completo do estudante.
    """
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
