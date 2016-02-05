from django.conf.urls import url
from .views import UserListView


urlpatterns = [
    # url(regex=r'^main/$',
    #     view=Main.as_view(),
    #     name='main'),
    url(regex=r'^user/list/$',
        view=UserListView.as_view(),
        name='user_list'),
    # url(regex=r'^user/(?P<pk>[0-9]+)/$',
    #     view=UserUpdate.as_view(),
    #     name='user_detail'),
    # url(regex=r'^project/create/$',
    #     view=.as_view(),
    #     name='project_create'),
    # url(regex=r'^project/list/$',
    #     view=.as_view(),
    #     name='project_list'),
    # url(regex=r'^project/(?P<pk>[0-9]+)/$',
    #     view=UserUpdate.as_view(),
    #     name='project_details')
    ]