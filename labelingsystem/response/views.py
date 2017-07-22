# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, FormView
from django.http import HttpResponseRedirect, HttpResponseNotFound

from .models import QuizResponse, QuestionResponse
from quiz.models import Quiz

# Create your views here.
class QuizResponseListView(ListView):
	model = QuizResponse
	template_name = 'response/quiz_response_list.html'

	def get_queryset(self):
		user = self.request.user
		self.quiz_response_list = user.profile.quiz_response_list.all()
		return self.quiz_response_list.all()

	def get_context_data(self, *args, **kwargs):
		context = super(QuizResponseListView, self).get_context_data(**kwargs)
		context["quiz_response_list"] = self.quiz_response_list
		return context

class QuizResponseDetailView(DetailView):
	model = QuizResponse
	template_name = 'response/quiz_response_detail.html'

	def dispatch(self, request, *args, **kwargs):
		self.quiz_response = get_object_or_404(QuizResponse, pk=self.kwargs['pk'])
		return super(QuizResponseDetailView, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		user = self.request.user
		self.question_response_list = QuestionResponse.objects.filter(user=self.quiz_response.user.pk, quiz_response=self.quiz_response).all()
		return self.question_response_list

	def get_context_data(self, *args, **kwargs):
		context = super(QuizResponseDetailView, self).get_context_data(**kwargs)
		context["question_response_list"] = self.question_response_list
		return context

def create_response(request, pk):
    if request.method == 'POST':

    	quiz = Quiz.objects.get(pk=pk)
        correct_count = 0
        question_list = quiz.question_list.all()
        question_response_list = []
        for question in question_list:
            question_response = QuestionResponse.objects.create(
                user = request.user,
                question = question,
                correct = request.POST.get("question_" + str(question.id)))

            if question_response.correct == "True":
                correct_count += 1

            question_response_list.append(question_response)

        quiz_response = QuizResponse.objects.create(
            user = request.user,
            quiz = quiz,
            score = correct_count/question_list.count()*100)

        for question_response in question_response_list:
            question_response.quiz_response.add(quiz_response)

        if quiz_response.score >= quiz.pass_mark:
            request.user.profile.quiz_response_list.add(quiz_response)

        return HttpResponseRedirect('/quiz/my_quiz_list')
    else:
        return HttpResponseNotFound("No label page can be retrieved")
