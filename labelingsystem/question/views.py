# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import FormView

from .models import Question
from answer.models import Answer
from .forms import CreateQuestionForm, UploadQuestionForm
from answer.forms import AnswerFormSet, AnswerFormSetHelper

import csv

# Create your views here.
class CreateQuestionView(FormView):
    model = Question
    template_name = 'question/create_question.html'
    success_url = '/question/create_question'
    form_class = CreateQuestionForm

    def get_context_data(self, **kwargs):
        data = super(CreateQuestionView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['answer_list'] = AnswerFormSet(self.request.POST)
            data['helper'] = AnswerFormSetHelper()
        else:
            data['answer_list'] = AnswerFormSet()
            data['helper'] = AnswerFormSetHelper()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        answer_list = context['answer_list']
        self.object = form.save()
        if answer_list.is_valid():
            answer_list.instance = self.object
            answer_list.save()

        return super(CreateQuestionView, self).form_valid(form)

class UploadQuestionView(FormView):
    model = Question
    template_name = 'question/upload_question.html'
    success_url = '/admin/question/question'
    form_class = UploadQuestionForm

    def form_valid(self, form):
        form = UploadQuestionForm(self.request.POST, self.request.FILES)
        self.parse_file(self.request.FILES['file'], self.request.user)
        return super(UploadQuestionView, self).form_valid(form)

    def parse_file(self, file, user):
        try:
            sep=b"|"
            reader = csv.reader(file, delimiter=sep, skipinitialspace=True)

            # read question_content, answer_content
            for line in reader:
                question_content = line[0]
                question = Question.objects.create(
                    content = question_content,
                    creator = user)

                answer_content = line[1]
                answer = Answer.objects.create(
                    question = question,
                    content = answer_content,
                    correct = True)

                for answer_item in line[2:]:
                    answer = Answer.objects.create(
                    question = question,
                    content = answer_item,
                    correct = False)


        except Exception, e:
            print("Fail parsing quiz file.")
            print(e)
            Exception(e)