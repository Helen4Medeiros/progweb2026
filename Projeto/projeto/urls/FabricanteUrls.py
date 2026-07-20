from django.urls import path
from projeto.views.FabricanteView import *

urlpatterns = [
    path("", list_fabricante_view, name="fabricante"),
    path("create", create_fabricante_view, name="create_fabricante"),
    path("edit/<int:id>", edit_fabricante_view, name="edit_fabricante"),
    path("details/<int:id>", details_fabricante_view, name="details_fabricante"),
    path("delete/<int:id>", delete_fabricante_view, name="delete_fabricante"),
]