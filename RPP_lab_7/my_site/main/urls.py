from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('index.html', index, name="home"),
    path('tables.html', tables, name="tables"),
    path('change_tab.html', change_tab, name="change_tab"),
    path('create_rec.html', create_rec, name="create_rec"),
    path('update_rec.html', update_rec, name="update_rec"),
]