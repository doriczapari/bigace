from bigaceproject.models import Project, UserProfile, Rating
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView


class ProjectListView(ListView):

    template_name = 'project_list.html'
    model = Project


class ProjectCreateView(CreateView):

    template_name = 'project_create.html'
    model = Project
    fields = ['name', 'description', 'owner', 'deadline', 'technologies',
              'max_people', 'created_at']

    # def get_success_url(self):
    #     return '/project/{0}'.format(self.object.id)


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


class UserUpdateView(UpdateView):

    template_name = 'user_update.html'
    model = UserProfile
    fields = ['user', 'skills', 'twitter', 'github']


class UserRateView(CreateView):

    template_name = 'user_rate.html'
    model = Rating
    fields = ['rating_to', 'point']
