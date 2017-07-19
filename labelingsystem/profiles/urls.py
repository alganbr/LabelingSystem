from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'profiles'

urlpatterns = [
	url(r'^username/(?P<username>[-\w]+)/$', views.ProfileDetailView.as_view(), name='profile'),
]