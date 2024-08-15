from rest_framework import viewsets, permissions
from .models import Student
from .serializers import StudentSerializer, StudentSerializerDetail


class StudentViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar as operações CRUD (Criar, Ler, Atualizar, Deletar) para o modelo `Student`.

    O `StudentViewSet` utiliza o `StudentSerializer` para serializar os dados dos estudantes e
    fornece endpoints de API RESTful que permitem interagir com as informações dos estudantes.
    O acesso a essas operações é restrito a usuários autenticados.

    Atributos:
        queryset (QuerySet): Consulta que retorna todos os objetos `Student` do banco de dados.
        serializer_class (Serializer): Define o `StudentSerializer` como o serializador a ser usado.
        permission_classes (list): Lista de classes de permissão aplicadas à ViewSet. Somente usuários autenticados têm permissão para acessar esses endpoints.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentSerializerDetail
        else:
            return StudentSerializer
