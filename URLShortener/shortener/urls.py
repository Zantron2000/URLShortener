from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name='home'),
    path("create", views.create_short_link),
    path("<str:link>", views.redirect_short_link)
]