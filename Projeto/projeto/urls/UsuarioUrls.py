from django.urls import path
from projeto.views.UsuarioView import list_usuario_view
urlpatterns = [
    path("", list_usuario_view, name='usuario'),
]