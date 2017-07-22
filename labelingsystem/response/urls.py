from django.conf.urls import url

from . import views

app_name = 'response'

urlpatterns = [
  url(r'^quiz_response_list/$', views.QuizResponseListView.as_view(), name='quiz_response_list'),
  url(r'^quiz_response_detail/(?P<pk>[-\w]+)$', views.QuizResponseDetailView.as_view(), name='quiz_response_detail'),
  url(r'^create_response/(?P<pk>[-\w]+)$', views.create_response, name='create_response'),
]