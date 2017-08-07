from django.conf.urls import url

from . import views

app_name = 'task'

urlpatterns = [
  url(r'^my_task_list/$', views.MyTaskListView.as_view(), name='my_task_list'),
  url(r'^task_record_list/$', views.TaskRecordListView.as_view(), name='task_record_list'),
  url(r'^take_task/(?P<pk>[-\w]+)$', views.TakeTaskView.as_view(), name='take_task'),
  url(r'^create_task/$', views.CreateTaskView.as_view(), name='create_task'),
  url(r'^owned_task_list/$', views.OwnedTaskListView.as_view(), name='owned_task_list'),
  url(r'^send_task/$', views.SendTaskView.as_view(), name='send_task'),
  url(r'^evaluate_task/(?P<pk>[-\w]+)$', views.EvaluateTaskView.as_view(), name='evaluate_task'),
]