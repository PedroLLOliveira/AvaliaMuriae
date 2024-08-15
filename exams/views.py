from rest_framework import viewsets, permissions
from .models import (
    QuestionTest,
    TestAnswerSheet,
    SchoolTest,
    StudentResponse
)
from .serializers import (
    QuestionSerializer,
    TestAnswerSheetSerializer,
    SchoolTestSerializer,
    StudentResponseSerializer
)

class StudentResponseViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar ou editar respostas de alunos.

    Este ViewSet fornece as operações padrão de CRUD (Create, Read, Update, Delete) 
    para o modelo StudentResponse. Somente usuários autenticados podem acessar este endpoint.

    Atributos:
        queryset (QuerySet): Conjunto de objetos de StudentResponse a serem manipulados.
        serializer_class (StudentResponseSerializer): Serializador utilizado para representar os dados de StudentResponse.
        permission_classes (list): Lista de classes de permissão que definem o acesso ao endpoint.
    """
    queryset = StudentResponse.objects.all()
    serializer_class = StudentResponseSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar ou editar questões de prova.

    Este ViewSet fornece as operações padrão de CRUD (Create, Read, Update, Delete) 
    para o modelo QuestionTest. Somente usuários autenticados podem acessar este endpoint.

    Atributos:
        queryset (QuerySet): Conjunto de objetos de QuestionTest a serem manipulados.
        serializer_class (QuestionSerializer): Serializador utilizado para representar os dados de QuestionTest.
        permission_classes (list): Lista de classes de permissão que definem o acesso ao endpoint.
    """
    queryset = QuestionTest.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestAnswerSheetViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar ou editar gabaritos de provas.

    Este ViewSet fornece as operações padrão de CRUD (Create, Read, Update, Delete) 
    para o modelo TestAnswerSheet. Somente usuários autenticados podem acessar este endpoint.

    Atributos:
        queryset (QuerySet): Conjunto de objetos de TestAnswerSheet a serem manipulados.
        serializer_class (TestAnswerSheetSerializer): Serializador utilizado para representar os dados de TestAnswerSheet.
        permission_classes (list): Lista de classes de permissão que definem o acesso ao endpoint.
    """
    queryset = TestAnswerSheet.objects.all()
    serializer_class = TestAnswerSheetSerializer
    permission_classes = [permissions.IsAuthenticated]


class SchoolTestViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar ou editar testes escolares.

    Este ViewSet fornece as operações padrão de CRUD (Create, Read, Update, Delete) 
    para o modelo SchoolTest. Somente usuários autenticados podem acessar este endpoint.

    Atributos:
        queryset (QuerySet): Conjunto de objetos de SchoolTest a serem manipulados.
        serializer_class (SchoolTestSerializer): Serializador utilizado para representar os dados de SchoolTest.
        permission_classes (list): Lista de classes de permissão que definem o acesso ao endpoint.
    """
    queryset = SchoolTest.objects.all()
    serializer_class = SchoolTestSerializer
    permission_classes = [permissions.IsAuthenticated]
