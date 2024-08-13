from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Administrator
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo `User`, que lida com a criação e validação de usuários.

    Este serializer serializa os campos básicos do modelo `User`, incluindo
    `id`, `username`, `email`, `password`, `first_name` e `last_name`.
    Ele também fornece validação personalizada e lógica de criação para
    lidar com a configuração de nomes de usuário.

    Atributos:
        Meta (class): Define o modelo `User` como base e especifica os campos a serem serializados.
        extra_kwargs (dict): Define que o campo `password` é de escrita única (write-only)
            e que `username` não é obrigatório.

    Métodos:
        validate(data): Valida os dados de entrada, garantindo que o `username`
            seja definido, usando `first_name` como fallback.
        create(validated_data): Cria um novo usuário usando os dados validados.
    """
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
      

class AdministratorSerializer(serializers.ModelSerializer):
  """
    Serializer para o modelo `Administrator`, que lida com a criação e serialização de administradores.

    Este serializer inclui o `UserSerializer` aninhado para gerenciar os dados do usuário
    associado ao administrador, e permite a criação de um novo `Administrator`
    juntamente com um novo `User`.

    Atributos:
        user (UserSerializer): Serializador aninhado que lida com a serialização
            e criação do objeto `User` associado ao `Administrator`.

        Meta (class): Define o modelo `Administrator` como base e serializa todos os campos.

    Métodos:
        create(validated_data): Cria um novo administrador e o usuário associado
            usando os dados validados.
    """
  user = UserSerializer()
  
  class Meta:
      model = Administrator
      fields = '__all__'

  def create(self, validated_data):
      user_data = validated_data.pop('user')
      user = User.objects.create_user(**user_data)
      administrator = Administrator.objects.create(user=user, **validated_data)
      return administrator
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer personalizado para obter tokens JWT, estendendo o `TokenObtainPairSerializer`.

    Esta classe adiciona informações extras ao token gerado, incluindo o `user_id`,
    `username`, e, se o usuário for um administrador, o `administrator_id`.

    Métodos:
        validate(attrs): Valida as credenciais do usuário e gera o token JWT.
            Se o usuário for um administrador, o ID do administrador é adicionado
            ao token. Também adiciona `user_id` e `username` ao token.
    """
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        try:
            administrator = Administrator.objects.get(user=user)
            data.update({'administrator_id': administrator.id})
        except Administrator.DoesNotExist:
            data.update({'administrator_id': None})

        data.update({'user_id': user.id})
        data.update({'username': user.username})
        return data
