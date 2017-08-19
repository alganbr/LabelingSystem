from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Fieldset, ButtonHolder, HTML, Button
from crispy_forms.bootstrap import FieldWithButtons, StrictButton

from .models import Task
from quiz.models import Quiz, AnswerKey, Answer
from label.models import Label
from post.models import Post

import csv
from io import TextIOWrapper

class CreateTaskForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(CreateTaskForm, self).__init__(*args, **kwargs)
		self.fields['Task Title'] = forms.CharField(max_length=50)
		self.fields['Task Description'] = forms.CharField(widget=forms.Textarea, required=False)
		self.fields['Upload Task Posts and Labels'] = forms.FileField()

		self.fields['Quiz Title'] = forms.CharField(max_length=50, required=False)
		self.fields['Quiz Description'] = forms.CharField(widget=forms.Textarea, required=False)
		self.fields['Max Posts'] = forms.IntegerField(required=False)
		self.fields['Pass Mark'] = forms.IntegerField(max_value=100, required=False)
		self.fields['Upload Quiz Posts and Labels'] = forms.FileField()

		self.fields['Participating Coders'] = forms.CharField(widget=forms.Textarea, required=False)

		self.helper = FormHelper()
		self.helper.form_id = 'create_task_form'
		self.helper.form_method = 'POST'
		self.helper.form_action = '/task/create_task/'
		self.helper.layout = Layout(
			HTML("""<div class="panel panel-info">
					<div class="panel-heading">
						Step 1: Create Task
					</div>
					<div class="panel-body">
					"""),
			Field('Task Title', placeholder="Enter the task title..."),
			Field('Task Description', placeholder="Write some description about the task..."),
			Field('Upload Task Posts and Labels'),
			HTML("""</div>
					</div>"""),
			HTML("""<div class="panel panel-info">
					<div class="panel-heading">
						Step 2: Create Quiz (Optional)
					</div>
					<div class="panel-body">
					<p> Note: This is an optional prerequisite quiz for the task </p>
					"""),
			Field('Quiz Title', placeholder="Enter the quiz title..."),
			Field('Quiz Description', placeholder="Write some description about the quiz..."),
			Field('Max Posts'),
			Field('Pass Mark'),
			Field('Upload Quiz Posts and Labels'),
			HTML("""</div>
					</div>"""),
			HTML("""<div class="panel panel-info">
					<div class="panel-heading">
						Step 3: Send Task
					</div>
					<div class="panel-body">
					<p> Note: Enter the coders to participate in the task line by line </p>
					"""),
			Field('Participating Coders', placeholder=" coder1@example.com \n coder2@example.com \n ..."),
			HTML("""</div>
					</div>"""),
			)
		self.helper.add_input(Submit('create_task_submit', 'Submit', css_class='btn btn-info btn-sm pull-right'))

	def create_quiz(self, quiz_title, quiz_description, max_posts, pass_mark, quiz_upload_file, user):
		try:
			quiz_object = Quiz.objects.create(
				title = quiz_title,
				description = quiz_description,
				max_posts = max_posts,
				pass_mark = pass_mark,
				creator = user)

			reader = csv.reader(TextIOWrapper(quiz_upload_file), delimiter='|', skipinitialspace=True)

			answer_key_object = AnswerKey.objects.create(quiz=quiz_object)

			label_list = []
			labels = next(reader)
			for label in labels:
				label_object = Label.objects.create(content=label)
				label_list.append(label_object)
				quiz_object.label_list.add(label_object)

			posts = reader
			for post in posts:
				post_object = Post.objects.create(
					content = post[0],
					author = user)
				quiz_object.post_list.add(post_object)
				answer_object = Answer.objects.create(
					answer_key = answer_key_object,
					post = post_object,
					label = [item for item in label_list if item.content == post[1]][0])
		except:
			return None

		return quiz_object

	def create_task(self, task_title, task_description, task_upload_file, user, prerequisite):
		task_object = Task.objects.create(
			title = task_title,
			description = task_description,
			prerequisite = prerequisite,
			creator = user)

		reader = csv.reader(TextIOWrapper(task_upload_file), delimiter='|', skipinitialspace=True)

		labels = next(reader)
		for label in labels:
			label_object = Label.objects.create(content=label)
			task_object.label_list.add(label_object)

		posts = reader
		for post in posts:
			post_object = Post.objects.create(
				content = post[0],
				author = user)
			task_object.post_list.add(post_object)

	def send_email(self):
		participating_coders = self.cleaned_data['Participating Coders']
		coder_list = participating_coders.split('\n')
		for coder in coder_list:
			print(coder)
