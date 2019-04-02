"""geekshop URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
import mainapp.views as mainapp

urlpatterns = [
	url(r'^$', mainapp.main, name='index'),
    #url(r'^index.html$', mainapp.main, name='index'),
    url(r'catalogue/index.html$', mainapp.catalogue, name='catalogue'),
    url(r'^contacts/index.html$', mainapp.contacts, name='contacts'),
    url(r'^admin/', admin.site.urls),
    url(r'catalogue/Monitor/Eizo ColorEdge CG318-4K/CG318-4K.html$', mainapp.monitor, name='CG318-4K'),
]
