from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from .models import Question

class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateQuestionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False

class UploadQuestionForm(forms.Form):
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
    	super(UploadQuestionForm, self).__init__(*args, **kwargs)

    	self.helper = FormHelper()
    	self.helper.form_id = "upload_question_form"
        self.helper.form_method = "POST"
        self.helper.form_action = "/question/upload_question/"
    	self.helper.add_input(Submit('upload_question_submit', 'Submit', css_class='btn btn-info btn-sm pull-right'))