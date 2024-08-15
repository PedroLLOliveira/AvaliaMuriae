from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Teacher
from .serializers import (
    TeacherSerializer,
    TeacherSerializerDetail,
    CustomTeacherTokenObtainPairSerializer
)

class TeacherViewSet(viewsets.ModelViewSet):
    """
      ViewSet para gerenciar operações CRUD no modelo `Teacher`.

      Esta classe fornece ações padrão como listar, criar, atualizar e deletar
      instâncias de professores. Está configurada para exigir que o usuário esteja
      autenticado para acessar essas operações.

      Atributos:
          queryset (QuerySet): Conjunto de dados que contém todos os professores.
          serializer_class (TeacherSerializer): Classe de serialização usada para
              transformar os dados do modelo `Teacher`.
          permission_classes (list): Lista de permissões necessárias para acessar esta view,
              exigindo que o usuário esteja autenticado.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TeacherSerializerDetail
        else:
            return TeacherSerializer


class RegisterTeacherView(APIView):
    """
    APIView para registrar um novo professor.

    Esta view permite que qualquer usuário, independentemente de estar autenticado,
    registre um novo professor no sistema. Ela valida os dados fornecidos e, se forem
    válidos, cria um novo professor.

    Métodos:
        post(request, *args, **kwargs): Recebe uma requisição POST com os dados do professor,
            valida esses dados e, se forem válidos, cria um novo professor. Retorna a resposta
            com os dados do professor criado ou os erros de validação.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    View personalizada para obter um par de tokens JWT, incluindo dados específicos do professor.

    Esta view estende o `TokenObtainPairView` padrão do Django Rest Framework
    e utiliza um serializer personalizado (`CustomTeacherTokenObtainPairSerializer`)
    para incluir informações adicionais no payload do token, como o ID do professor.

    Atributos:
        serializer_class (CustomTeacherTokenObtainPairSerializer): Classe de serialização usada para
            adicionar informações extras ao token JWT.
    """
    serializer_class = CustomTeacherTokenObtainPairSerializer
