from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Fieldset, ButtonHolder, HTML, Button
from crispy_forms.bootstrap import FieldWithButtons, StrictButton

from .models import *

class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        exclude = ['creator']

    def __init__(self, *args, **kwargs):
        super(CreateQuizForm, self).__init__(*args, **kwargs)
        self.fields["upload_question"] = forms.FileField()

        self.helper = FormHelper()
        self.helper.form_id = "create_quiz_form"
        self.helper.form_method = "POST"
        self.helper.form_action = "/quiz/create_quiz/"
        self.helper.layout = Layout(
            Field('title'),
            Field('description'),
            FieldWithButtons('category', StrictButton("""<span class="glyphicon glyphicon-plus" data-toggle="modal" data-target="#category_modal"></span>""", css_class="btn btn-info btn-sm")),
            Field('max_questions'),
            Field('pass_mark'),
            Field('random_order'),
            Field('single_attempt'),
            FieldWithButtons('question_list', StrictButton("""<span class="glyphicon glyphicon-plus" data-toggle="modal" data-target="#question_modal"></span>""", css_class="btn btn-info btn-sm")),
            StrictButton("""<span class="glyphicon glyphicon-plus" data-toggle="modal" data-target="#upload_question_modal"> Upload Questions</span>""", css_class="btn btn-warning btn-sm"),
        )
        self.helper.add_input(Submit('create_quiz_submit', 'Submit', css_class='btn btn-info btn-sm pull-right'))

class SendQuizForm(forms.Form):
    send_to = forms.ModelMultipleChoiceField(User.objects.all(), label="Send To", widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(SendQuizForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-info btn-sm pull-right'))

class TakeQuizForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(TakeQuizForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-info btn-sm pull-right'))