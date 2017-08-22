from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView

from .forms import SignUpForm, AccountPasswordChangeForm
from task.models import Participation
from response.models import PostResponse

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:login')

class AccountDetailView(LoginRequiredMixin, DetailView):
	model = User
	template_name = 'account/account_detail.html'
	fields = ('email', )

	def dispatch(self, request, *args, **kwargs):
		user = self.request.user
		self.task_list = Participation.objects.filter(coder=user).values_list('task', flat=True)
		self.post_response_list = PostResponse.objects.filter(responder=user)
		return super(AccountDetailView, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(AccountDetailView, self).get_context_data(**kwargs)
		context['task_list'] = self.task_list
		context['post_response_list'] = self.post_response_list
		return context

class AccountPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
	form_class = AccountPasswordChangeForm
	template_name = 'account/password_change.html'
	success_url = reverse_lazy('account:password_change_success')

class AccountPasswordChangeSuccessView(LoginRequiredMixin, TemplateView):
	template_name = 'account/password_change_success.html'
