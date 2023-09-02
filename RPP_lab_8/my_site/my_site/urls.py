"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView

from main.views import *
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', views.tables, name='home'),
    path('edit/', TemplateView.as_view(template_name="editing.html"), name='edit'),
    path('register/', Register.as_view(), name='register'),
    # Страницы редактирования
    path('users/', views.Tabs.in_users, name='users'),
    path('posts/', views.Tabs.in_posts, name='posts'),
    path('topics/', views.Tabs.in_topics, name='topics'),
    path('authors/', views.Tabs.in_authors, name='authors'),
    path('comments/', views.Tabs.in_comments, name='comments'),
    # Страница удаления
    path('delete_<int:tb>_<int:id>/', views.Tabs.delete, name='delete'),
    # Страница изменения
    path('update_<int:tb>_<int:id>/', views.Tabs.update, name='update'),
    # Страница создания
    path('create_<int:tb>/', views.Tabs.create, name='create'),
    # Сохранение
    path('save_<int:tb>_<int:new_id>/', views.Tabs.save, name='save'),

]
