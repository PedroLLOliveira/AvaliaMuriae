from rest_framework import serializers
from school.serializers import (
  SchoolSerializer,
  ClassRoomSerializer  
)
from school.models import (
  School,
  ClassRoom
)
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo `Student`, transformando os dados do estudante em formatos
    compatíveis com JSON para serem usados em APIs.

    O `StudentSerializer` inclui os detalhes da escola (`SchoolSerializer`) e da sala de aula
    (`ClassRoomSerializer`) associadas ao estudante, permitindo que essas informações sejam
    incluídas nas respostas da API.

    Atributos:
        school (SchoolSerializer): Serializador aninhado que representa a escola do estudante.
        class_room (ClassRoomSerializer): Serializador aninhado que representa a sala de aula do estudante.

    Meta:
        model (Student): Define o modelo `Student` que será serializado.
        fields (str): Especifica que todos os campos do modelo devem ser incluídos na serialização.
    """
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    class_room = serializers.PrimaryKeyRelatedField(queryset=ClassRoom.objects.all())
    
    class Meta:
      model = Student
      fields = '__all__'


class StudentSerializerDetail(serializers.ModelSerializer):
    """
    Serializador para o modelo `Student`, transformando os dados do estudante em formatos
    compatíveis com JSON para serem usados em APIs.

    O `StudentSerializer` inclui os detalhes da escola (`SchoolSerializer`) e da sala de aula
    (`ClassRoomSerializer`) associadas ao estudante, permitindo que essas informações sejam
    incluídas nas respostas da API.

    Atributos:
        school (SchoolSerializer): Serializador aninhado que representa a escola do estudante.
        class_room (ClassRoomSerializer): Serializador aninhado que representa a sala de aula do estudante.

    Meta:
        model (Student): Define o modelo `Student` que será serializado.
        fields (str): Especifica que todos os campos do modelo devem ser incluídos na serialização.
    """
    school = SchoolSerializer()
    class_room = ClassRoomSerializer()
    
    class Meta:
      model = Student
      fields = '__all__'
