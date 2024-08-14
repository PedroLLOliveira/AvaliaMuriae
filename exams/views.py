from rest_framework import viewsets, permissions
from .models import (
  Question,
  TestAnswerSheet,
  SchoolTest
)
from .serializers import (
  QuestionSerializer,
  TestAnswerSheetSerializer,
  SchoolTestSerializer
)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestAnswerSheetViewSet(viewsets.ModelViewSet):
    queryset = TestAnswerSheet.objects.all()
    serializer_class = TestAnswerSheetSerializer
    permission_classes = [permissions.IsAuthenticated]


class SchoolTestViewSet(viewsets.ModelViewSet):
    queryset = SchoolTest.objects.all()
    serializer_class = SchoolTestSerializer
    permission_classes = [permissions.IsAuthenticated]
