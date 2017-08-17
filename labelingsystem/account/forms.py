from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from cuser.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

User = get_user_model()

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'login-form'

        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('email', placeholder="e-mail"),
            Field('password', placeholder="Password")
        )
        self.helper.add_input(Submit('submit', 'Sign in', css_class='btn btn-info btn-sm pull-right'))

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-info btn-sm pull-right'))