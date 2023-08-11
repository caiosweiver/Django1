"""
URL configuration for NAMEOFPROEJECT project.

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

from django.urls import path, include
from myapp.views import *
from loginsys.views import *
from django.contrib import admin

urlpatterns = [
    path('posts/', post_list.as_view(), name='post_list'),
    path('posts/<int:pk>', post_ref.as_view(), name='post_ref'),
    path('posts/user', my_posts.as_view(), name='my_posts'),
    path('posts/create', create_posts.as_view(), name='create_posts'),
    path('posts/<int:pk>/edit', edit_posts.as_view(), name='edit_posts'),
    path('posts/<int:pk>/delete', delete_posts.as_view(), name='delete_posts'),
    path('admin/', admin.site.urls),
    path('about/', about_page, name='about'),
    path('', homepage, name='homepage'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/register', Register_user.as_view(), name='register_page'),
]

