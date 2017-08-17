from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Quiz
from task.models import Task
from post.models import Post
from label.models import Label

import random

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class TakeQuizView(LoginRequiredMixin, TemplateView):
	model = Quiz
	template_name = 'quiz/take_quiz.html'

	def dispatch(self, request, *args, **kwargs):
		self.quiz = get_object_or_404(Quiz, pk=self.kwargs['pk'])
		return super(TakeQuizView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(TakeQuizView, self).get_context_data(**kwargs)
		post_list = get_list_or_404(self.quiz.post_list.all())
		random.shuffle(post_list)
		context['quiz'] = self.quiz
		context['post_list'] = post_list
		context['label_list'] = self.quiz.label_list.all()
		return context


class QuizSuccessView(LoginRequiredMixin, TemplateView):
	model = Quiz
	template_name = 'quiz/quiz_success.html'

	def dispatch(self, request, *args, **kwargs):
		self.quiz = get_object_or_404(Quiz, pk=self.kwargs['pk'])
		self.task = Task.objects.get(prerequisite=self.quiz.pk)
		return super(QuizSuccessView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(QuizSuccessView, self).get_context_data(**kwargs)
		context['quiz'] = self.quiz
		context['task'] = self.task
		return context

class QuizFailView(LoginRequiredMixin, TemplateView):
	model = Quiz
	template_name = 'quiz/quiz_fail.html'

	def dispatch(self, request, *args, **kwargs):
		self.quiz = get_object_or_404(Quiz, pk=self.kwargs['pk'])
		return super(QuizFailView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(QuizFailView, self).get_context_data(**kwargs)
		context['quiz'] = self.quiz
		return context


