from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'profile'

urlpatterns = [
	url(r'^profile_detail/(?P<username>[-\w]+)/$', views.ProfileDetailView.as_view(), name='profile_detail'),
]