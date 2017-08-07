from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Fieldset, ButtonHolder, HTML, Button
from crispy_forms.bootstrap import FieldWithButtons, StrictButton

from .models import *

from django.contrib.auth import get_user_model
User = get_user_model()

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', )

	def __init__(self, *args, **kwargs):
		super(UserUpdateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_tag = False
		# self.helper.form_class = 'form-horizontal'
		# self.helper.label_class = 'col-md-2'
		# self.helper.field_class = 'col-md-8'
		self.helper.form_id = "profile_update_form"
		self.helper.form_method = "POST"
		self.helper.form_action = "/profile/profile_detail/"

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('profile_pic', )

	def __init__(self, *args, **kwargs):
		super(ProfileUpdateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_tag = False
		# self.helper.form_class = 'form-horizontal'
		# self.helper.label_class = 'col-md-2'
		# self.helper.field_class = 'col-md-8'
		self.helper.form_id = "profile_update_form"
		self.helper.form_method = "POST"
		self.helper.form_action = "/profile/profile_detail/"
