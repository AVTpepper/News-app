"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from news_blog.views import index, login, sign_up, article_view, post_creation, view_all
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', index, name="index"),
    path('login/', auth_views.LoginView.as_view(
        template_name='news_blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='news_blog/logout.html'), name='logout'),
    path('sign-up/', sign_up, name='sign_up'),
    path('article-view/', article_view, name='article_view'),
    path('post-creation/', post_creation, name='post_creation'),
    path('view-all-posts/', view_all, name='view_all'),
]
