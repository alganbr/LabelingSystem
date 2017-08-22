from django.conf.urls import url

from .views import *

app_name = 'task'

urlpatterns = [
  url(r'^task_list/$', TaskListView.as_view(), name='task_list'),
  url(r'^take_task/(?P<pk>[-\w]+)$', TakeTaskView.as_view(), name='take_task'),
  url(r'^task_complete/$', TaskCompleteView.as_view(), name='task_complete'),
  url(r'^task_empty/$', TaskEmptyView.as_view(), name='task_empty'),
  url(r'^create_task/$', CreateTaskView.as_view(), name='create_task'),
  url(r'^create_task_success/$', CreateTaskSuccessView.as_view(), name='create_task_success'),
  url(r'^task_evaluation_list/$', TaskEvaluationListView.as_view(), name='task_evaluation_list'),
  url(r'^task_evaluation_empty/$', TaskEvaluationEmptyView.as_view(), name='task_evaluation_empty'),
  url(r'^task_evaluation_detail/(?P<pk>[-\w]+)$', TaskEvaluationDetailView.as_view(), name='task_evaluation_detail'),
]