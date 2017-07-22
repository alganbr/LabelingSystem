# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, FormView

from .models import Category
from .forms import CreateCategoryForm

# Create your views here.
class CreateCategoryView(FormView):
    model = Category
    template_name = 'category/create_category.html'
    success_url = '/category/create_category'
    form_class = CreateCategoryForm

    def form_valid(self, form):
        category = form.save(commit=False)
        category.save()
        return super(CreateCategoryView, self).form_valid(form)
