from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('<int:quiz_id>/take/', views.take_quiz, name='take_quiz'),
    path('result/<int:attempt_id>/', views.quiz_result, name='quiz_result'),
]
