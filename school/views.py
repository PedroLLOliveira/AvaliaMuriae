from rest_framework import viewsets, permissions
from .models import School
from .serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
  """
    ViewSet para gerenciar operações CRUD no modelo `School`.

    Esta classe fornece ações padrão como listar, criar, atualizar e deletar
    instâncias de escolas. Está configurada para exigir que o usuário esteja
    autenticado para acessar essas operações.

    Atributos:
        queryset (QuerySet): Conjunto de dados que contém todas as escolas.
        serializer_class (SchoolSerializer): Classe de serialização usada para
            transformar os dados do modelo `School`.
        permission_classes (list): Lista de permissões necessárias para acessar esta view,
            exigindo que o usuário esteja autenticado.
  """
  queryset = School.objects.all()
  serializer_class = SchoolSerializer
  permission_classes = [permissions.IsAuthenticated]
