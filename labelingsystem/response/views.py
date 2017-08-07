# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, FormView
from django.http import HttpResponseRedirect, HttpResponseNotFound

from .models import QuizResponse, QuizQuestionResponse, TaskResponse, TaskQuestionResponse
from quiz.models import Quiz
from task.models import Task
from answer.models import Answer

# Create your views here.
class QuizResponseDetailView(DetailView):
	model = QuizResponse
	template_name = 'response/quiz_response_detail.html'

	def dispatch(self, request, *args, **kwargs):
		self.quiz_response = get_object_or_404(QuizResponse, pk=self.kwargs['pk'])
		return super(QuizResponseDetailView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super(QuizResponseDetailView, self).get_context_data(**kwargs)
		context["quiz_response"] = self.quiz_response
		context["question_response_list"] = QuizQuestionResponse.objects.filter(user=self.quiz_response.user.pk, quiz_response=self.quiz_response).all()
		return context

def create_quiz_response(request, pk):
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
                    answer = answer,
                    correct = answer.correct,
                    quiz_response = quiz_response)
            except:
                pass

        if quiz.single_attempt is True:
            request.user.profile.quiz_list.remove(quiz)

        return HttpResponseRedirect('/quiz/my_quiz_list')
    else:
        return HttpResponseNotFound("No label page can be retrieved")

class TaskResponseDetailView(DetailView):
    model = TaskResponse
    template_name = 'response/task_response_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.task_response = get_object_or_404(TaskResponse, pk=self.kwargs['pk'])
        return super(TaskResponseDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(TaskResponseDetailView, self).get_context_data(**kwargs)
        context["task_response"] = self.task_response
        context["question_response_list"] = TaskQuestionResponse.objects.filter(user=self.task_response.user.pk, task_response=self.task_response).all()
        return context

def create_task_response(request, pk):
    if request.method == 'POST':

        task = Task.objects.get(pk=pk)
        question_list = task.question_list.all()

        task_response = TaskResponse.objects.create(
            user = request.user,
            task = task)

        for question in question_list:
            try:
                answer_id = request.POST.get("question_" + str(question.id))
                answer = get_object_or_404(Answer, pk=answer_id)
                question_response = TaskQuestionResponse.objects.create(
                    user = request.user,
                    question = question,
                    answer = answer,
                    task_response = task_response)
            except:
                pass

        request.user.profile.task_list.remove(task)

        return HttpResponseRedirect('/task/my_task_list')
    else:
        return HttpResponseNotFound("No label page can be retrieved")
