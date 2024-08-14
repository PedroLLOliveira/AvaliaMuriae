from rest_framework import serializers
from school.serializers import (
  SchoolSerializer,
  ClassRoomSerializer  
)
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
  school = SchoolSerializer()
  class_room = ClassRoomSerializer()
  
  class Meta:
    model = Student
    fields = '__all__'
