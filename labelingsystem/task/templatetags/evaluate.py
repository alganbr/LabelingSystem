# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

import random
from django import template
from response.models import TaskQuestionResponse
register = template.Library()

@register.simple_tag
def evaluate(answer, question, task_response_list):
	if len(task_response_list) is 0:
		return "N/A"

	count = 0
	for task_response in task_response_list:
		task_question_response_list = TaskQuestionResponse.objects.filter(task_response=task_response.pk, question=question.pk, answer=answer.pk)
		count += len(task_question_response_list)

	return "{0}%".format(count/len(task_response_list)*100)
    