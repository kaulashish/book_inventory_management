from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", HomePage.as_view(), name="homepage"),
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("addstore/", AddStore.as_view(), name="addstore"),
    path("<int:pk>/store-view/", StoreView.as_view(), name="store-view"),
    path("<int:pk>/search-book/", SearchBook.as_view(), name="home"),
    path("book-info/", BookInfo.as_view(), name="book-info"),
    path("add/", BookAdd.as_view(), name="book-add"),
    path(
        "<int:pk>/delete", DeleteInventoryItem.as_view(), name="delete-inventory-item"
    ),
    path("<int:pk>/edit", EditInventoryItem.as_view(), name="edit-inventory-item"),
]
