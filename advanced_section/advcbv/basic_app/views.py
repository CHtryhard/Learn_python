from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model=models.School
    # without the context it return lower case of School + _list: school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    # without the context it return lower case of School
    model = models.School

    template_name = 'basic_app/school_detail.html'
