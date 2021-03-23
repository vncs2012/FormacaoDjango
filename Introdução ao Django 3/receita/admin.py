from django.contrib import admin

from .models import Receita


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria',
                    'tempo_preparo', 'pessoa', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_filter = ('categoria', 'pessoa')
    list_editable = ('publicada',)
    list_per_page = 5


admin.site.register(Receita, ReceitaAdmin)
