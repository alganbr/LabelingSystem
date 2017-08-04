# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, FormView
from django.http import HttpResponseRedirect, HttpResponseNotFound

from .models import QuizResponse, QuizQuestionResponse
from quiz.models import Quiz
from answer.models import Answer

# Create your views here.
class QuizResponseListView(ListView):
	model = QuizResponse
	template_name = 'response/quiz_response_list.html'

	def get_queryset(self):
		user = self.request.user
		self.quiz_response_list = QuizResponse.objects.filter(user=user)
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

	def get_context_data(self, *args, **kwargs):
		context = super(QuizResponseDetailView, self).get_context_data(**kwargs)
		context["quiz_response"] = self.quiz_response
		context["question_response_list"] = QuizQuestionResponse.objects.filter(user=self.request.user.pk, quiz_response=self.quiz_response).all()
		return context

def create_response(request, pk):
    if request.method == 'POST':

    	quiz = Quiz.objects.get(pk=pk)
        correct_count = 0
        question_list = quiz.question_list.all()

        question_count = len(question_list)
        if quiz.max_questions and (quiz.max_questions < len(question_list)):
            question_count = quiz.max_questions

        for question in question_list:
            try:
                answer_id = request.POST.get("question_" + str(question.id))
                answer = get_object_or_404(Answer, pk=answer_id)

                if answer.correct is True:
                    correct_count += 1
            except:
                pass

        quiz_response = QuizResponse.objects.create(
            user = request.user,
            quiz = quiz,
            score = correct_count/question_count * 100)

        for question in question_list:
            try:
                answer_id = request.POST.get("question_" + str(question.id))
                answer = get_object_or_404(Answer, pk=answer_id)
                question_response = QuizQuestionResponse.objects.create(
                    user = request.user,
                    question = question,
                    correct = answer.correct,
                    quiz_response = quiz_response)
            except:
                pass

        if quiz.single_attempt is True:
            request.user.profile.quiz_list.remove(quiz)

        return HttpResponseRedirect('/quiz/my_quiz_list')
    else:
        return HttpResponseNotFound("No label page can be retrieved")
