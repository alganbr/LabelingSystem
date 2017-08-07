from django.conf.urls import url

from . import views

app_name = 'response'

urlpatterns = [
  url(r'^quiz_response_detail/(?P<pk>[-\w]+)$', views.QuizResponseDetailView.as_view(), name='quiz_response_detail'),
  url(r'^create_quiz_response/(?P<pk>[-\w]+)$', views.create_quiz_response, name='create_quiz_response'),
  url(r'^create_task_response/(?P<pk>[-\w]+)$', views.create_task_response, name='create_task_response'),
  url(r'^task_response_detail/(?P<pk>[-\w]+)$', views.TaskResponseDetailView.as_view(), name='task_response_detail'),
]