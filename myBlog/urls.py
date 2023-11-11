"""
URL configuration for myBlog project.

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
from django.urls import path

from blog.views import saludar_con_html
from blog.views import profile, articles, create, details, login, panel,  about, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', saludar_con_html, name="inicio"),
    path('articles/', articles, name="articles"),
    path('profile/', profile, name="profile"),
    path('create/', create, name="create"),
    path('details/', details, name="details"),
    path('login/', login, name="login"),
    path('panel/', panel, name="panel"),
    path('about/', about, name="about"),
    path('register/', register, name="register"),
]
