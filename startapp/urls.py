"""
URL configuration for startapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simplechat/', include('apps.simplechat.urls')),
    path('chatterbot/', include('apps.chatterbot.urls')),
    path('nltkbot/', include('apps.nltkbot.urls')),
    path('scikit_learn/', include('apps.scikit_learn.urls')),
    path('sat_vader/', include('apps.sat_vader.urls')),
]
