"""labelingsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from . import views
from . import forms

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', auth_views.LoginView.as_view(template_name='login.html', redirect_field_name='home', form_class=forms.LoginForm, redirect_authenticated_user=True), name='login'),
    url(r'^login$', auth_views.LoginView.as_view(template_name='login.html', redirect_field_name='home', form_class=forms.LoginForm, redirect_authenticated_user=True), name='login'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^home/$', views.HomePage.as_view(), name='home'),
    url(r'^profile/', include('profile.urls', namespace='profile')),
    url(r'^quiz/', include('quiz.urls', namespace='quiz')),
    url(r'^category/', include('category.urls', namespace='category')),
    url(r'^question/', include('question.urls', namespace='question')),
    url(r'^answer/', include('answer.urls', namespace='answer')),
    url(r'^response/', include('response.urls', namespace='response')),
    url(r'^task/', include('task.urls', namespace='task')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
