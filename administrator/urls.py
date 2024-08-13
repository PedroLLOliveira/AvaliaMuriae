from django.urls import path
from .views import (
  AdministratorViewSet,
  RegisterAdministratorView,
  CustomTokenObtainPairView
)
from rest_framework_simplejwt.views import TokenRefreshView

administrator_list = AdministratorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
administrator_detail = AdministratorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('administrator/', administrator_list, name='administrator-list'),
    path('administrator/<str:pk>/', administrator_detail, name='administrator-detail'),
    path('register/', RegisterAdministratorView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
