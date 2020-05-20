from django.contrib import admin
from .models import Post, Agenda, Categoriasagenda

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'full_name', 'categories']
    search_fields = ['title', 'sub_title']
    #fields = ('title', 'sub_title')

class AgendaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'data', 'valor', 'categoria']

admin.site.register(Post, PostAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Categoriasagenda)

