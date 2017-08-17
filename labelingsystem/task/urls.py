from django.conf.urls import url

from .views import *

app_name = 'task'

urlpatterns = [
  url(r'^task_list/$', TaskListView.as_view(), name='task_list'),
  url(r'^take_task/(?P<pk>[-\w]+)$', TakeTaskView.as_view(), name='take_task'),
  url(r'^task_complete/$', TaskCompleteView.as_view(), name='task_complete'),
  url(r'^task_empty/$', TaskEmptyView.as_view(), name='task_empty'),
]