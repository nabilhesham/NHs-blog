"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from blog import views

urlpatterns = [
    path('<post_id>/post_edit', views.post_edit, name='post_edit'),
    path('<post_id>/post_delete', views.post_delete, name='post_delete'),
    path('<id>/favourite_post', views.favourite_post, name='favourite_post'),
    path('<p_id>/<p_slug>', views.post_detail, name='post_detail'),
    path('post_create', views.post_create, name='post_create'),
    path('edit_profile',views.edit_profile, name='edit_profile'),
    path('favourites', views.favourite_post_list, name='favourite_post_list'),
]
