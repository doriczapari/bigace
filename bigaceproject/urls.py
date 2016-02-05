from django.conf.urls import url
from .views import UserListView, UserCreateView, UserDetailView, UserUpdateView
from .views import ProjectCreateView, UserRateView, ProjectListView


urlpatterns = [
    # url(regex=r'^main/$',
    #     view=Main.as_view(),
    #     name='main'),
    url(regex=r'^user/new/',
        view=UserCreateView.as_view(),
        name='user_create'),
    url(regex=r'^user/list/$',
        view=UserListView.as_view(),
        name='user_list'),
    url(regex=r'^user/(?P<pk>[0-9]+)/$',
        view=UserDetailView.as_view(),
        name='user_detail'),
    url(regex=r'^user/update/(?P<pk>[0-9]+)/$',
        view=UserUpdateView.as_view(),
        name='user_update'),
    url(regex=r'^rate/$',
        view=UserRateView.as_view(),
        name='user_rate'),
    url(regex=r'^project/create/$',
        view=ProjectCreateView.as_view(),
        name='project_create'),
    url(regex=r'^project/list/$',
        view=ProjectListView.as_view(),
        name='project_list'),
    url(regex=r'^user/(?P<pk>[0-9]+)/$',
        view=UserDetailView.as_view(),
        name='user_detail'),
    # url(regex=r'^project/(?P<pk>[0-9]+)/$',
    #     view=UserUpdate.as_view(),
    #     name='project_details')
    ]
