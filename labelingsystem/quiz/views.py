# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, FormView, TemplateView

import random

from .models import Quiz, Question
from .forms import CreateQuizForm, SendQuizForm
from category.models import Category
from profile.models import Profile
from response.models import QuizResponse
from category.forms import CreateCategoryForm
from question.forms import CreateQuestionForm, UploadQuestionForm
from answer.forms import AnswerFormSet, AnswerFormSetHelper

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class CreateQuizView(FormView):
    model = Quiz
    template_name = 'quiz/create_quiz.html'
    success_url = '/quiz/create_quiz'
    form_class = CreateQuizForm

    def get_context_data(self, **kwargs):
        context = super(CreateQuizView, self).get_context_data(**kwargs)
        context["category_form"] = CreateCategoryForm
        context["question_form"] = CreateQuestionForm
        context["answer_list"] = AnswerFormSet()
        context["helper"] = AnswerFormSetHelper()
        context["upload_question_form"] = UploadQuestionForm
        return context

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
        quiz_response_list = QuizResponse.objects.filter(user=user)
        completed_quiz_list = []
        for quiz_response in quiz_response_list:
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

    def dispatch(self, request, *args, **kwargs):
        self.quiz = get_object_or_404(Quiz, pk=self.kwargs['pk'])
        return super(TakeQuizView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TakeQuizView, self).get_context_data(**kwargs)
        context["quiz"] = self.quiz
        question_list = list(self.quiz.question_list.all())

        if self.quiz.random_order is True:
            random.shuffle(question_list)

        if self.quiz.max_questions and (self.quiz.max_questions < len(question_list)):
            question_list = question_list[:self.quiz.max_questions]

        context["question_list"] = question_list
        return context

class QuizSuccessView(TemplateView):
    template_name = 'quiz/quiz_success.html'

class QuizFailView(TemplateView):
    template_name = 'quiz/quiz_fail.html'


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
    success_url = '/admin/quiz/quiz'
    form_class = SendQuizForm

    def dispatch(self, request, *args, **kwargs):
        quiz_string = request.GET.get('ids')
        try:
            self.quiz_list = quiz_string.split(',')
        except:
            self.quiz_list = []

        return super(SendQuizView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SendQuizView, self).get_context_data(**kwargs)
        context["quiz_list"] = self.quiz_list
        return context

    def form_valid(self, form):
        receiver_list = form.cleaned_data['send_to']
        for quiz in self.quiz_list:
            try:

                for receiver in receiver_list:
                    receiver.profile.quiz_list.add(quiz)
            except:
                pass
        return super(SendQuizView, self).form_valid(form)

class QuizRecordListView(ListView):
    model = QuizResponse
    template_name = 'quiz/quiz_record_list.html'
    success_url = '/quiz/quiz_record_list'

    def get_queryset(self):
        user = self.request.user
        self.quiz_record_list = QuizResponse.objects.filter(user=user).order_by('-created_at')
        return self.quiz_record_list.all()

    def get_completed_quizzes(self):
        user = self.request.user
        completed_quiz_list = []
        for quiz_response in self.quiz_record_list:
            if quiz_response.score > quiz_response.quiz.pass_mark:
                completed_quiz_list.append(quiz_response.quiz)
        return completed_quiz_list

    def get_context_data(self, **kwargs):
        context = super(QuizRecordListView, self).get_context_data(**kwargs)
        context["quiz_record_list"] = self.quiz_record_list
        context["completed_quiz_list"] = self.get_completed_quizzes()
        return context






