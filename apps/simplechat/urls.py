from django.urls import path
from . import views

app_name = 'simplechat'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_response/', views.get_response, name='get_response'),
]