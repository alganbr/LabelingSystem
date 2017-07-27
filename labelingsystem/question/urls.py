from django.conf.urls import url

from . import views

app_name = 'question'

urlpatterns = [
  url(r'^create_question/$', views.CreateQuestionView.as_view(), name='create_question'),
  url(r'^upload_question/$', views.UploadQuestionView.as_view(), name='upload_question'),
]