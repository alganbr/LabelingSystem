from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('account:login')
    template_name = 'signup.html'
