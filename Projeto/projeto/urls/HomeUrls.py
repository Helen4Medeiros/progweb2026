from django.urls import path
from projeto.views.HomeView import home_view


urlpatterns = [
path("", home_view),
]