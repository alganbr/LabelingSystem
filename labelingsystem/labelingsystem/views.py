from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
	template_name = 'index.html'

class AdminIndexView(LoginRequiredMixin, TemplateView):
	template_name = 'admin_index.html'