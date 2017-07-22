# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from . import models
from . import forms

# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
	model = User
	template_name = 'profile/profile_update.html'

class ProfileDetailView(DetailView):
	model = User
	template_name = 'profile/profile_detail.html'
	slug_field = 'username'
	slug_url_kwarg = 'username'
	context_object_name = 'user'

	def get_object(self):
		return User.objects.get(username=self.kwargs.get('username'))

	def get_context_data(self, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(**kwargs)
		return context

class ProfileListView(ListView):
	model = User
	template_name = 'profile/profile_list.html'
	success_url = reverse_lazy('login')
