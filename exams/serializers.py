from rest_framework import serializers
from .models import (
  Question,
  TestAnswerSheet,
  SchoolTest
)
from student.serializers import StudentSerializer


class QuestionSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Question
    fields = '__all__'


class TestAnswerSheetSerializer(serializers.ModelSerializer):
  correct_answer = QuestionSerializer(many=True)
  
  class Meta:
    model = TestAnswerSheet
    fields = '__all__'


class SchoolTestSerializer(serializers.ModelSerializer):
  student = StudentSerializer()
  student_response = QuestionSerializer(many=True)
  
  class Meta:
    model = SchoolTest
    fields = '__all__'
