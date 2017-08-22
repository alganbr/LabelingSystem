from django.conf.urls import url

from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from .forms import *

app_name = 'account'

urlpatterns = [
    url(r'^login$', LoginView.as_view(template_name='account/login.html', redirect_field_name='home', form_class=LoginForm, redirect_authenticated_user=True), name='login'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^logout/$', LogoutView.as_view(redirect_field_name='account:login'), name='logout'),
    url(r'^account_detail/(?P<pk>[-\w]+)/$', AccountDetailView.as_view(), name='account_detail'),
    url(r'^password_change/$', AccountPasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change_success/$', AccountPasswordChangeSuccessView.as_view(), name='password_change_success')
]