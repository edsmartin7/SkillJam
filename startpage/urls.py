
from django.conf.urls import url
from . import views

urlpatterns = [

   #url(r'^$', views.StartPageHandler, name='musician'),
   url(r'^(?P<user_id>[0-9]+)/$', views.user_profile, name='user'),
   url(r'^$', views.all_profile, name='all'),

]

#fix user_id regex

