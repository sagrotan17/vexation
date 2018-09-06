from django.conf.urls import url
from django.urls import path, re_path, include

from . import views

app_name='mixed'

urlpatterns = [
    path('',views.home, name='home'),

]