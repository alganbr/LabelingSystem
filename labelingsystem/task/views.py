# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, FormView

from .models import Task, Question
from .forms import CreateTaskForm, SendTaskForm
from category.models import Category
from profile.models import Profile
from response.models import TaskResponse
from category.forms import CreateCategoryForm
from question.forms import CreateQuestionForm, UploadQuestionForm
from answer.forms import AnswerFormSet, AnswerFormSetHelper

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class CreateTaskView(FormView):
    model = Task
    template_name = 'task/create_task.html'
    success_url = '/task/create_task'
    form_class = CreateTaskForm

    def get_context_data(self, **kwargs):
        context = super(CreateTaskView, self).get_context_data(**kwargs)
        context["category_form"] = CreateCategoryForm
        context["question_form"] = CreateQuestionForm
        context["answer_list"] = AnswerFormSet()
        context["helper"] = AnswerFormSetHelper()
        context["upload_question_form"] = UploadQuestionForm
        return context

    def form_valid(self, form):
        task = form.save(commit=False)
        task.creator = self.request.user
        task.save()
        form.save_m2m()
        return super(CreateTaskView, self).form_valid(form)

class MyTaskListView(ListView):
    model = Task
    template_name = 'task/my_task_list.html'

    def get_queryset(self):
        user = self.request.user
        self.task_list = user.profile.task_list.all()
        return self.task_list.all()

    def get_completed_tasks(self):
        user = self.request.user
        completed_task_list = user.profile.task_response_list.all()
        return completed_task_list

    def get_context_data(self, **kwargs):
        context = super(MyTaskListView, self).get_context_data(**kwargs)
        context["task_list"] = self.task_list 
        context["completed_task_list"] = self.get_completed_tasks()
        return context

class TakeTaskView(ListView):
    model = Question
    template_name = 'task/take_task.html'
    success_url = '/task/my_task_list'

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=self.kwargs['pk'])
        return super(TakeTaskView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TakeTaskView, self).get_context_data(**kwargs)
        context["task"] = self.task
        context["question_list"] = self.task.question_list.all()
        return context

class OwnedTaskListView(ListView):
    model = Task
    template_name = 'task/owned_task_list.html'

    def get_queryset(self):
        user = self.request.user
        self.task_list = Task.objects.filter(creator=user)
        return self.task_list.all()

    def get_context_data(self, **kwargs):
        context = super(OwnedTaskListView, self).get_context_data(**kwargs)
        context["task_list"] = self.task_list
        return context

class SendTaskView(FormView):
    model = Task
    template_name = 'task/send_task.html'
    success_url = '/task/owned_task_list'
    form_class = SendTaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=self.kwargs['pk'])
        return super(SendTaskView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SendTaskView, self).get_context_data(**kwargs)
        context["task"] = self.task
        return context

    def form_valid(self, form):
        receiver = form.cleaned_data['send_to']
        receiver.profile.task_list.add(self.task)
        return super(SendTaskView, self).form_valid(form)

class TaskRecordListView(ListView):
    model = TaskResponse
    template_name = 'task/task_record_list.html'
    success_url = '/task/task_record_list'

    def get_queryset(self):
        user = self.request.user
        self.task_record_list = user.profile.task_response_list.all()
        return self.task_record_list.all()

    def get_completed_taskzes(self):
        user = self.request.user
        completed_task_list = user.profile.task_response_list.filter()
        completed_task_list = []
        for task_response in user.profile.task_response_list.all():
            if task_response.score > task_response.task.pass_mark:
                completed_task_list.append(task_response.task)
        return completed_task_list

    def get_context_data(self, **kwargs):
        context = super(TaskRecordListView, self).get_context_data(**kwargs)
        context["task_record_list"] = self.task_record_list
        context["completed_task_list"] = self.get_completed_taskzes()
        return context