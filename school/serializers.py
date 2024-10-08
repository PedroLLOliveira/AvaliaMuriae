from rest_framework import serializers
from .models import School, ClassRoom


class SchoolSerializer(serializers.ModelSerializer):
  """
    Serializer para o modelo `School`, que lida com a serialização e deserialização dos dados da escola.

    Este serializer converte instâncias do modelo `School` em representações
    JSON e vice-versa, facilitando a interação com APIs RESTful.

    Meta:
        model (School): Define o modelo `School` como base para este serializer.
        fields (str): Especifica que todos os campos do modelo `School` devem ser incluídos na serialização.
  """
  
  class Meta:
    model = School
    fields = '__all__'


class ClassRoomSerializer(serializers.ModelSerializer):
  """
    Serializer para o modelo `ClassRoom`, que lida com a serialização e deserialização dos dados da sala de aula.

    Este serializer converte instâncias do modelo `ClassRoom` em representações
    JSON e vice-versa, facilitando a interação com APIs RESTful.

    Meta:
        model (ClassRoom): Define o modelo `ClassRoom` como base para este serializer.
        fields (str): Especifica que todos os campos do modelo `ClassRoom` devem ser incluídos na serialização.
  """
  class Meta:
    model = ClassRoom
    fields = '__all__'