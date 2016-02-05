from bigaceproject.models import Project
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView
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

    def get_success_url(self):
        return '/user/{0}'.format(self.object.id)


class UserDetailView(DetailView):
    template_name = 'user_details.html'
    model = User
