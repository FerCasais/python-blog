from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.urls import reverse

from blog.models import Article

from django.db.models import Q





# Create your views here.
def saludar_con_html(request):
    contexto = {
      
    }
    Http_Response= render(
        request=request,
        template_name='inicio.html',
        context=contexto)
    return Http_Response



def about(request):
    contexto = {
           
    }
    http_response = render(
        request=request,
        template_name="about.html",
        context=contexto,
    )
    return http_response

def articles(request):
    contexto = {
           
    }
    http_response = render(
        request=request,
        template_name="articles.html",
        context=contexto,
    )
    return http_response

def details(request):
    contexto = {
           
    }
    http_response = render(
        request=request,
        template_name="details.html",
        context=contexto,
    )
    return http_response

def create(request):
    contexto = {
           
    }
    http_response = render(
        request=request,
        template_name="create.html",
        context=contexto,
    )
    return http_response

def register(request):
    contexto = {
           
    }
    http_response = render(
        request=request,
        template_name="register.html",
        context=contexto,
    )
    return http_response

def login(request):
    contexto = {
           
    }
    http_response = render(
        request=request,
        template_name="login.html",
        context=contexto,
    )
    return http_response

def profile(request):
    contexto = {
           
    }
    http_response = render(
        request=request,
        template_name="profile.html",
        context=contexto,
    )
    return http_response

def panel(request):
    contexto = {
           
    }
    http_response = render(
        request=request,
        template_name="panel.html",
        context=contexto,
    )
    return http_response


