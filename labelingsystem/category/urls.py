from django.conf.urls import url

from . import views

app_name = 'category'

urlpatterns = [
  url(r'^create_category/$', views.CreateCategoryView.as_view(), name='create_category'),
]