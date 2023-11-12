from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': 'Главная страница', 'url_name': 'main_page'},
        {'title': 'О сайте', 'url_name': 'about_page'},
        {'title': 'Добавить запись', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact_page'},
        {'title': 'Войти', 'url_name': 'login_page'}]


def main_page(request):
    posts = Artist.objects.all()
    genres = Genre.objects.all()
    context = {
        'title': 'Main page',
        'posts': posts,
        'genres': genres,
        'menu': menu,
        'select_url': 0
    }
    return render(request, 'music/index_main.html', context=context)


def about_page(request):
    genres = Genre.objects.all()
    context = {
        'title': 'About page',
        'genres': genres,
        'menu': menu,
    }
    return render(request, 'music/index_about.html', context=context)


def add_page(request):
    return HttpResponse('Add page')


def contact_page(request):
    return HttpResponse('Contact page')


def login_page(request):
    return HttpResponse('Login page')


def post_page(request, post_id):
    return HttpResponse('Post page, post id {}'.format(post_id))


def genre_page(request, genre_id):
    posts = Artist.objects.filter(genre__id=genre_id)
    genres = Genre.objects.all()

    if not posts:
        raise Http404

    context = {
        'title': 'Main page',
        'posts': posts,
        'genres': genres,
        'menu': menu,
        'select_url': genre_id
    }
    return render(request, 'music/index_main.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
