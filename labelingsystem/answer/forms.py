from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from django.forms.models import inlineformset_factory

from .models import Answer
from question.models import Question

class CreateAnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = '__all__'
		exclude = ['question']

AnswerFormSet = inlineformset_factory(Question, Answer, form=CreateAnswerForm, extra=4)

class AnswerFormSetHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(AnswerFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'POST'
        self.form_tag = False