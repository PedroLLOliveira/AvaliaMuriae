from django.urls import path
from .views import (
  SchoolViewSet,
  ClassRoomViewSet
)

school_list = SchoolViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
school_detail = SchoolViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
classRoom_list = ClassRoomViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
classRoom_detail = ClassRoomViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('school/', school_list, name='school-list'),
    path('school/<str:pk>/', school_detail, name='school-detail'),
    path('classRoom/', classRoom_list, name='classRoom-list'),
    path('classRoom/<str:pk>/', classRoom_detail, name='classRoom-detail'),
]
