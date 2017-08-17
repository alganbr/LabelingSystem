from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView
from .models import Task, Participation
from post.models import Post
from response.models import PostResponse

import random
from django.db.models import Q

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class TaskListView(LoginRequiredMixin, ListView):
	model = Task
	template_name = 'task/task_list.html'

	def dispatch(self, request, *args, **kwargs):
		user = self.request.user
		try:
			task_ids = Participation.objects.filter(coder=user.pk).values('task').distinct()
			get_list_or_404(task_ids)
			self.task_list = Task.objects.filter(id__in=task_ids)
			get_list_or_404(self.task_list)
		except:
			return redirect('/task/task_empty', permanent=True)

		return super(TaskListView, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		return self.task_list

	def get_context_data(self, **kwargs):
		context = super(TaskListView, self).get_context_data(**kwargs)
		context['task_list'] = self.get_queryset()
		return context

class TakeTaskView(LoginRequiredMixin, TemplateView):
	model = Task
	template_name = 'task/take_task.html'

	def dispatch(self, request, *args, **kwargs):
		self.task = get_object_or_404(Task, pk=self.kwargs['pk'])

		post_response_ids = PostResponse.objects.filter(task=self.task.pk, responder=self.request.user.pk).values_list('post__id', flat=True).distinct()
		try:
			post_list = get_list_or_404(self.task.post_list.filter(~Q(id__in=post_response_ids)))
			random.shuffle(post_list)
			self.post = post_list[0]
		except:
			return redirect('/task/task_complete', permanent=True)

		return super(TakeTaskView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(TakeTaskView, self).get_context_data(**kwargs)
		context['task'] = self.task
		context['post'] = self.post
		context['label_list'] = self.task.label_list.all()
		return context

class TaskCompleteView(LoginRequiredMixin, TemplateView):
    template_name = 'task/task_complete.html'

class TaskEmptyView(LoginRequiredMixin, TemplateView):
    template_name = 'task/task_empty.html'

