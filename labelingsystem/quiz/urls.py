from django.conf.urls import url

from . import views

app_name = 'quiz'

urlpatterns = [
  url(r'^my_quiz_list/$', views.MyQuizListView.as_view(), name='my_quiz_list'),
  url(r'^quiz_record_list/$', views.QuizRecordListView.as_view(), name='quiz_record_list'),
  url(r'^take_quiz/(?P<pk>[-\w]+)$', views.TakeQuizView.as_view(), name='take_quiz'),
  url(r'^quiz_success/$', views.QuizSuccessView.as_view(), name='quiz_success'),
  url(r'^quiz_fail/$', views.QuizFailView.as_view(), name='quiz_fail'),
  url(r'^create_quiz/$', views.CreateQuizView.as_view(), name='create_quiz'),
  url(r'^owned_quiz_list/$', views.OwnedQuizListView.as_view(), name='owned_quiz_list'),
  url(r'^send_quiz/$', views.SendQuizView.as_view(), name='send_quiz'),
]