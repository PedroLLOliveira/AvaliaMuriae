from django.urls import path
from .views import (
  StudentViewSet,
)

student_list = StudentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
student_detail = StudentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('student/', student_list, name='student-list'),
    path('student/<str:pk>/', student_detail, name='student-detail'),
]
