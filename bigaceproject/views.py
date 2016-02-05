from bigaceproject.models import Project
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView
from . import models


class ProjectListView(ListView):

    template_name = 'project_list.html'
    model = Project


class UserListView(ListView):
    template_name = 'user_list.html'
    model = User


class UserCreateView(CreateView):

    template_name = 'user_create.html'
    model = User
    fields = ['username', 'email']
    success_url = '/'   # FIXME