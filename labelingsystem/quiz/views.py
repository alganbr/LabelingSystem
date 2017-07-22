# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, FormView

from .models import Quiz, Question
from .forms import CreateQuizForm, SendQuizForm
from category.models import Category
from profile.models import Profile

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class CreateQuizView(FormView):
    model = Quiz
    template_name = 'quiz/create_quiz.html'
    success_url = '/quiz/create_quiz'
    form_class = CreateQuizForm

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.creator = self.request.user
        quiz.save()
        form.save_m2m()
        return super(CreateQuizView, self).form_valid(form)

class MyQuizListView(ListView):
    model = Quiz
    template_name = 'quiz/my_quiz_list.html'

    def get_queryset(self):
        user = self.request.user
        self.quiz_list = user.profile.quiz_list.all()
        return self.quiz_list.all()

    def get_completed_quizzes(self):
        user = self.request.user
        completed_quiz_list = user.profile.quiz_response_list.filter()
        completed_quiz_list = []
        for quiz_response in user.profile.quiz_response_list.all():
            if quiz_response.score > quiz_response.quiz.pass_mark:
                completed_quiz_list.append(quiz_response.quiz)
        return completed_quiz_list

    def get_context_data(self, **kwargs):
        context = super(MyQuizListView, self).get_context_data(**kwargs)
        context["quiz_list"] = self.quiz_list 
        context["completed_quiz_list"] = self.get_completed_quizzes()
        return context

class TakeQuizView(ListView):
    model = Question
    template_name = 'quiz/take_quiz.html'
    success_url = '/quiz/my_quiz_list.html'

    def dispatch(self, request, *args, **kwargs):
        self.quiz = get_object_or_404(Quiz, pk=self.kwargs['pk'])
        return super(TakeQuizView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TakeQuizView, self).get_context_data(**kwargs)
        context["quiz"] = self.quiz
        context["question_list"] = self.quiz.question_list.all()
        return context

class OwnedQuizListView(ListView):
    model = Quiz
    template_name = 'quiz/owned_quiz_list.html'

    def get_queryset(self):
        user = self.request.user
        self.quiz_list = Quiz.objects.filter(creator=user)
        return self.quiz_list.all()

    def get_context_data(self, **kwargs):
        context = super(OwnedQuizListView, self).get_context_data(**kwargs)
        context["quiz_list"] = self.quiz_list
        return context

class SendQuizView(FormView):
    model = Quiz
    template_name = 'quiz/send_quiz.html'
    success_url = '/quiz/owned_quiz_list'
    form_class = SendQuizForm

    def dispatch(self, request, *args, **kwargs):
        self.quiz = get_object_or_404(Quiz, pk=self.kwargs['pk'])
        return super(SendQuizView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SendQuizView, self).get_context_data(**kwargs)
        context["quiz"] = self.quiz
        return context

    def form_valid(self, form):
        receiver = form.cleaned_data['send_to']
        receiver.profile.quiz_list.add(self.quiz)
        return super(SendQuizView, self).form_valid(form)





