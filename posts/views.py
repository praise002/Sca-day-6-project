from django.shortcuts import render
from django.views.generic import ListView
from . models import Post


class HomePageView(ListView):
    model = Post  #it returns <model>_list that can be itr over
    template_name = 'home.html'