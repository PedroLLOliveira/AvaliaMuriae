from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Teacher
from school.serializers import (
  SchoolSerializer,
  ClassRoomSerializer
)
from school.models import School, ClassRoom
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}, 'username': {'required': False}}

    def validate(self, data):
        if 'username' not in data or not data['username']:
            data['username'] = data.get('first_name', '')
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TeacherSerializer(serializers.ModelSerializer):
  """
    Serializer para o modelo `Teacher`, que lida com a serialização e deserialização dos dados do professor.

    Este serializer converte instâncias do modelo `Teacher` em representações
    JSON e vice-versa, facilitando a interação com APIs RESTful. Ele também
    serializa os dados do usuário associado, escolas e salas de aula.

    Atributos:
        user (UserSerializer): Serializador aninhado para o modelo `User`.
        schools (SchoolSerializer): Serializador aninhado para o modelo `School`, permitindo
            a serialização de várias escolas associadas ao professor.
        class_rooms (ClassRoomSerializer): Serializador aninhado para o modelo `ClassRoom`, permitindo
            a serialização de várias salas de aula associadas ao professor.

    Meta:
        model (Teacher): Define o modelo `Teacher` como base para este serializer.
        fields (str): Especifica que todos os campos do modelo `Teacher` devem ser incluídos na serialização.

    Métodos:
        create(validated_data): Cria e retorna uma nova instância de `Teacher`, criando
            também o usuário associado com os dados validados.
  """
  user = UserSerializer()
  schools = serializers.PrimaryKeyRelatedField(many=True, queryset=School.objects.all())
  class_rooms = serializers.PrimaryKeyRelatedField(many=True, queryset=ClassRoom.objects.all())
  
  class Meta:
    model = Teacher
    fields = '__all__'

  def create(self, validated_data):
      user_data = validated_data.pop('user')
      schools_data = validated_data.pop('schools')
      class_rooms_data = validated_data.pop('class_rooms')

      # Criando o usuário
      user = User.objects.create_user(**user_data)

      # Criando o Teacher sem atribuir os campos ManyToMany
      teacher = Teacher.objects.create(user=user, **validated_data)

      # Atribuindo as escolas e salas de aula usando set()
      teacher.schools.set(schools_data)
      teacher.class_rooms.set(class_rooms_data)

      return teacher


class TeacherSerializerDetail(serializers.ModelSerializer):
  """
    Serializer para o modelo `Teacher`, que lida com a serialização e deserialização dos dados do professor.

    Este serializer converte instâncias do modelo `Teacher` em representações
    JSON e vice-versa, facilitando a interação com APIs RESTful. Ele também
    serializa os dados do usuário associado, escolas e salas de aula.

    Atributos:
        user (UserSerializer): Serializador aninhado para o modelo `User`.
        schools (SchoolSerializer): Serializador aninhado para o modelo `School`, permitindo
            a serialização de várias escolas associadas ao professor.
        class_rooms (ClassRoomSerializer): Serializador aninhado para o modelo `ClassRoom`, permitindo
            a serialização de várias salas de aula associadas ao professor.

    Meta:
        model (Teacher): Define o modelo `Teacher` como base para este serializer.
        fields (str): Especifica que todos os campos do modelo `Teacher` devem ser incluídos na serialização.

    Métodos:
        create(validated_data): Cria e retorna uma nova instância de `Teacher`, criando
            também o usuário associado com os dados validados.
  """
  user = UserSerializer()
  schools = SchoolSerializer(many=True)
  class_rooms = ClassRoomSerializer(many=True)
  
  class Meta:
    model = Teacher
    fields = '__all__'

  def create(self, validated_data):
      user_data = validated_data.pop('user')
      user = User.objects.create_user(**user_data)
      teacher = Teacher.objects.create(user=user, **validated_data)
      return teacher

class CustomTeacherTokenObtainPairSerializer(TokenObtainPairSerializer):
  """
    Serializer personalizado para obter um par de tokens JWT, incluindo dados específicos do professor.

    Este serializer estende o `TokenObtainPairSerializer` padrão do Django Rest Framework
    e adiciona informações adicionais no payload do token, como o ID do professor associado
    ao usuário autenticado.

    Métodos:
        validate(attrs): Valida as credenciais do usuário, adiciona o ID do professor
            ao token se o usuário for um professor, e também inclui o ID e nome de usuário do usuário.
  """
  def validate(self, attrs):
      data = super().validate(attrs)
      user = self.user

      try:
          teacher = Teacher.objects.get(user=user)
          data.update({'teacher_id': teacher.id})
      except Teacher.DoesNotExist:
          data.update({'teacher_id': None})

      data.update({'user_id': user.id})
      data.update({'username': user.username})
      return data
