from django.conf.urls import url
from .views import root_catagories, get_category

urlpatterns = [
    url(r'^$', root_catagories, name='categories'),
    url(r'^(?P<id>\d+)$', get_category, name='category'),
]