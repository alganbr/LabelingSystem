from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView, FormView, DetailView
from .models import Task, Participation
from label.models import Label
from post.models import Post
from response.models import PostResponse

from .forms import CreateTaskForm

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
			task_ids = Participation.objects.filter(coder=user.email).values('task').distinct()
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

class CreateTaskView(LoginRequiredMixin, FormView):
	model = Task
	form_class = CreateTaskForm
	template_name = 'task/create_task.html'
	success_url = '/task/create_task_success'

	def form_valid(self, form):
		task_title = form.cleaned_data['Task Title']
		task_description = form.cleaned_data['Task Description']
		task_upload_file = form.cleaned_data['Upload Task Posts and Labels']
		quiz_title = form.cleaned_data['Quiz Title']
		quiz_description = form.cleaned_data['Quiz Description']
		max_posts = form.cleaned_data['Max Posts']
		pass_mark = form.cleaned_data['Pass Mark']
		quiz_upload_file = form.cleaned_data['Upload Quiz Posts and Labels']
		participating_coders = form.cleaned_data['Participating Coders']

		prerequisite = form.create_quiz(quiz_title, quiz_description, max_posts, pass_mark, quiz_upload_file, self.request.user)
		task = form.create_task(task_title, task_description, task_upload_file, self.request.user, prerequisite)
		form.send_email(task)

		return super(CreateTaskView, self).form_valid(form)

class CreateTaskSuccessView(LoginRequiredMixin, TemplateView):
	template_name = 'task/create_task_success.html'

class TaskEvaluationListView(LoginRequiredMixin, ListView):
	model = Task
	template_name = 'task/task_evaluation_list.html'

	def dispatch(self, request, *args, **kwargs):
		user = self.request.user
		try:
			task_ids = Participation.objects.filter(coder=user.email).values('task').distinct()
			get_list_or_404(task_ids)
			self.task_list = Task.objects.filter(id__in=task_ids)
			get_list_or_404(self.task_list)
		except:
			return redirect('/task/task_empty', permanent=True)

		return super(TaskEvaluationListView, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		return self.task_list

	def get_context_data(self, **kwargs):
		context = super(TaskEvaluationListView, self).get_context_data(**kwargs)
		context['task_list'] = self.get_queryset()
		return context

class TaskEvaluationDetailView(LoginRequiredMixin, DetailView):
	model = Task
	template_name = 'task/task_evaluation_detail.html'
