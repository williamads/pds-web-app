"""pds_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pds_web.views import home
from pds_web.views import script
from pds_web.views import convolution_request
from pds_web.views import z_transform_request
from pds_web.views import discretize_request


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('script', script),
    path('convolution', convolution_request),
    path('z-transform', z_transform_request),
    path('discretize', discretize_request),
]




#urlpatterns = [
#    url(r'^$', pages.home, name='home_page'),
#    url(r'^rack/(?P<rack_name>\w+)/start/$', pages.start, name='start_page'),
#]
