from django.urls import path
from .views import (
  QuestionViewSet,
  TestAnswerSheetViewSet,
  SchoolTestViewSet
)

question_list = QuestionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
question_detail = QuestionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
testanswersheet_list = TestAnswerSheetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
testanswersheet_detail = TestAnswerSheetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
schooltest_list = SchoolTestViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
schooltest_detail = SchoolTestViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('question/', question_list, name='question-list'),
    path('question/<str:pk>/', question_detail, name='question-detail'),
    path('testanswersheet/', testanswersheet_list, name='testanswersheet-list'),
    path('testanswersheet/<str:pk>/', testanswersheet_detail, name='testanswersheet-detail'),
    path('schooltest/', schooltest_list, name='schooltest-list'),
    path('schooltest/<str:pk>/', schooltest_detail, name='schooltest-detail'),
]
