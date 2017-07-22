# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import FormView

from .models import Question
from .forms import CreateQuestionForm
from answer.forms import AnswerFormSet, AnswerFormSetHelper

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