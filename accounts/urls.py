
from django.conf.urls import url
from .views import logout, register, login, profile

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^login', login, name='login'),
    url(r'^profile/$', profile, name='profile'),
   
]