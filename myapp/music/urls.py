from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('about/', about_page, name='about_page'),
    path('add/', add_page, name='add_page'),
    path('contact/', contact_page, name='contact_page'),
    path('login/', login_page, name='login_page'),
    path('post/<int:post_id>/', post_page, name='post_page'),
    path('genre/<int:genre_id>/', genre_page, name='genre_page'),
]
