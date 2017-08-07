# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, FormView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()

class ProfileUpdateView(LoginRequiredMixin, FormView):
	model = User
	template_name = 'profile/profile_update.html'

	def get_context_data(self, **kwargs):
		context = super(ProfileUpdateView, self).get_context_data(**kwargs)
		return context

class ProfileDetailView(UpdateView):
	model = User
	template_name = 'profile/profile_detail.html'
	fields = ('first_name', 'last_name')
	slug_field = 'username'
	slug_url_kwarg = 'username'

	def get_object(self):
		return User.objects.get(username=self.kwargs.get('username'))

	def get_context_data(self, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(**kwargs)
		context["user_form"] = UserUpdateForm(self.request.POST or None, instance=self.get_object())
		context["profile_form"] = ProfileUpdateForm(self.request.POST or None, self.request.FILES, instance=self.get_object().profile)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		context = self.get_context_data()
		user_form = context['user_form']
		profile_form = context['profile_form']
		if user_form.is_valid():
			user_form.save()

		if profile_form.is_valid():
			profile_form.save()

		return super(ProfileDetailView, self).form_valid(profile_form)

	def get_success_url(self, **kwargs):
		return reverse_lazy('profile:profile_detail', kwargs={'username': self.request.user.username})

class ProfileListView(ListView):
	model = User
	template_name = 'profile/profile_list.html'
	success_url = reverse_lazy('login')
