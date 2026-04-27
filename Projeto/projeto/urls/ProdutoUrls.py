from django.urls import path
from projeto.views.ProdutoView import list_produto_view

urlpatterns = [

    path("", list_produto_view),
    path("<int:id>", list_produto_view),

]