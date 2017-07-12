"""ecom_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import say_hello
from accounts import urls as accounts_urls
from products import urls as products_urls
from django.views import static
from .settings import MEDIA_ROOT
from cart import urls as cart_urls
from payments import urls as payments_urls
from blog.views import im_home
from blog import urls as blog_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', say_hello, name='index'),
    url(r'accounts/', include(accounts_urls)),
    url(r'^store/', include(products_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'^cart/', include(cart_urls)),
    url(r'^payments/', include(payments_urls)),
    url(r'^blog/', include(blog_urls)),
    
]
