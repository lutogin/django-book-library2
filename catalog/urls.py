from django.urls import path, re_path
from catalog import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('book/'),
    # path('authors/'),
]
