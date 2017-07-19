# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView

from . import forms

class SignUp(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class HomePage(TemplateView):
	template_name = 'home.html'