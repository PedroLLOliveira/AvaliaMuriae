from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Administrator
from .serializers import AdministratorSerializer, CustomTokenObtainPairSerializer


class AdministratorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar operações CRUD no modelo `Administrator`.

    Esta classe fornece ações padrão como listar, criar, atualizar e deletar
    administradores. Está configurada para exigir autenticação para todas as
    operações.

    Atributos:
        queryset (QuerySet): Conjunto de dados que contém todos os administradores.
        serializer_class (AdministratorSerializer): Classe de serialização usada para
            transformar os dados do modelo `Administrator`.
        permission_classes (list): Lista de permissões necessárias para acessar esta view,
            que neste caso, exige que o usuário esteja autenticado.
    """
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterAdministratorView(APIView):
    """
    APIView para registrar um novo administrador.

    Esta classe lida com requisições POST para criar um novo `Administrator`.
    A criação de um administrador não exige autenticação, permitindo que qualquer
    usuário acesse este endpoint.

    Atributos:
        permission_classes (list): Lista de permissões necessárias para acessar esta view,
            permitindo acesso irrestrito (AllowAny).

    Métodos:
        post(request, *args, **kwargs): Recebe os dados do administrador, valida-os
            e cria um novo registro se os dados forem válidos. Retorna os dados
            do administrador criado ou os erros de validação.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = AdministratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    View personalizada para obter tokens JWT usando o `CustomTokenObtainPairSerializer`.

    Esta view é responsável por gerenciar as requisições de obtenção de tokens,
    utilizando o serializer personalizado que adiciona informações extras ao token.

    Atributos:
        serializer_class (CustomTokenObtainPairSerializer): Classe de serialização utilizada
            para validar as credenciais e gerar o token JWT com informações adicionais.
    """
    serializer_class = CustomTokenObtainPairSerializer
