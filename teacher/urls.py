from django.urls import path
from .views import (
  TeacherViewSet,
  RegisterTeacherView,
  CustomTokenObtainPairView
)
from rest_framework_simplejwt.views import TokenRefreshView

teacher_list = TeacherViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
teacher_detail = TeacherViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('teacher/', teacher_list, name='teacher-list'),
    path('teacher/<str:pk>/', teacher_detail, name='teacher-detail'),
    path('register/teacher/', RegisterTeacherView.as_view(), name='register'),
    path('login/teacher/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('teacher/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
