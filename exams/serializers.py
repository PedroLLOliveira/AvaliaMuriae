from rest_framework import serializers
from .models import (
  QuestionTest,
  TestAnswerSheet,
  SchoolTest,
  StudentResponse
)
from student.serializers import StudentSerializer


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Question. 

    Este serializer converte instâncias do modelo Question para formatos como JSON e também 
    valida dados de entrada antes de salvar ou atualizar instâncias de Question.

    Meta:
        model (Question): O modelo que está sendo serializado.
        fields (str): Serializa todos os campos do modelo Question.
    """
    class Meta:
      model = QuestionTest
      fields = '__all__'


class TestAnswerSheetSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo TestAnswerSheet. 

    Este serializer converte instâncias do modelo TestAnswerSheet para formatos como JSON e também 
    valida dados de entrada antes de salvar ou atualizar instâncias de TestAnswerSheet.

    Atributos:
        correct_answer (QuestionSerializer): Serializa as questões corretas associadas ao gabarito.

    Meta:
        model (TestAnswerSheet): O modelo que está sendo serializado.
        fields (str): Serializa todos os campos do modelo TestAnswerSheet.
    """
    correct_answer = QuestionSerializer(many=True)
    
    class Meta:
        model = TestAnswerSheet
        fields = '__all__'



class StudentResponseSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo StudentResponse.

    Este serializer converte instâncias do modelo StudentResponse para formatos como JSON e também 
    valida dados de entrada antes de salvar ou atualizar instâncias de StudentResponse.

    Atributos:
        question_reference (QuestionSerializer): Serializa a questão associada à resposta do aluno.

    Meta:
        model (StudentResponse): O modelo que está sendo serializado.
        fields (str): Serializa todos os campos do modelo StudentResponse.
    """
    question_reference = QuestionSerializer()
    
    class Meta:
        model = StudentResponse
        fields = '__all__'


class SchoolTestSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo SchoolTest. 

    Este serializer converte instâncias do modelo SchoolTest para formatos como JSON e também 
    valida dados de entrada antes de salvar ou atualizar instâncias de SchoolTest.

    Atributos:
        student (StudentSerializer): Serializa o aluno associado ao teste.
        student_response (StudentResponseSerializer): Serializa as respostas do aluno no teste.

    Meta:
        model (SchoolTest): O modelo que está sendo serializado.
        fields (str): Serializa todos os campos do modelo SchoolTest.
    """
    student = StudentSerializer()
    student_response = StudentResponseSerializer(many=True)
    
    class Meta:
        model = SchoolTest
        fields = '__all__'

