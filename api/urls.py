from django.urls import path
from . import views

urlpatterns = [
    path('book', views.BookList.as_view()),
    path('book/<int:id>', views.BookDetail.as_view()),
    path('author', views.AuthorList.as_view()),
    path('author/<int:id>', views.AuthorDetail.as_view())
]
