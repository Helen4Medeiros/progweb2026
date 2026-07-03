from django.contrib import admin
# senha: 702142mh
from .models import * #imporata nossos models

class FabricanteAdmin(admin.ModelAdmin):
# Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao',
    'preco', 'categoria',)
    search_fields = ('Produto',)
    fields = ('Produto', 'destaque', 'promocao',
'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'

admin.site.register(Categoria)
admin.site.register(Fabricante,FabricanteAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario)

