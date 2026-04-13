from django.contrib import admin
# senha: 702142mh
from .models import * #imporata nossos models
admin.site.register(Fabricante) #adiciona a interface do adm
admin.site.register(Categoria)
admin.site.register(Produto)
