from django.urls import path
from .views import BookList,BookListIV

urlpatterns = [
    path('list/',BookList.as_view(),name="book_list"),
    path('list/<int:pk>/',BookListIV.as_view(),name="book_detail"),

] 