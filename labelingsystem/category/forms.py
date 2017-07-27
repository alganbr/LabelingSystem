from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from .models import *

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateCategoryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = "create_category_form"
        self.helper.form_method = "POST"
        self.helper.form_action = "/category/create_category/"
        self.helper.add_input(Submit('create_category_submit', 'Submit', css_class='btn btn-info btn-sm pull-right'))