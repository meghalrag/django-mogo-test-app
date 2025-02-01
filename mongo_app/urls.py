from django.urls import path
from .views import user_form_view, user_list_view

urlpatterns = [
    path("add-user/", user_form_view, name="user_form"),
    path("users/", user_list_view, name="user_list"),
]
