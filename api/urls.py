from django.urls import path
from django.conf.urls import url
from . import views
from .api import CountView


urlpatterns = [
    path('counter', CountView.as_view(), name='counter'),
    url('', views.home_swagger)
]

