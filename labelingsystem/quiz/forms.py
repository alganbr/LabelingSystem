from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from .models import *

class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        exclude = ['creator']

    def __init__(self, *args, **kwargs):
        super(CreateQuizForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-info btn-sm pull-right'))

class SendQuizForm(forms.Form):
    send_to = forms.ModelChoiceField(User.objects.all(), label="Send To")

    def __init__(self, *args, **kwargs):
        super(SendQuizForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-info btn-sm pull-right'))

class TakeQuizForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(TakeQuizForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-info btn-sm pull-right'))

class UploadFileForm(forms.Form):
    file = forms.FileField()