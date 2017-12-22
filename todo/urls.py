from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.activity_list, name='activity_list'),
    url(r'^activity/(?P<pk>\d+)/$', views.activity_detail, name='activity_detail'),
    url(r'^activity/new/$', views.add_new, name='add_new'),
]
