from django.conf.urls import url

from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView
from .forms import LoginForm

app_name = 'account'

urlpatterns = [
    url(r'^login$', LoginView.as_view(template_name='login.html', redirect_field_name='home', form_class=LoginForm, redirect_authenticated_user=True), name='login'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^logout/$', LogoutView.as_view(redirect_field_name='account:login'), name='logout'),
]