from django.contrib import admin
from .models import Personaggi
# Register your models here.
# admin.site.register(Personaggi)


@admin.register(Personaggi)
class PersonaggiAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    list_display = ('nome','sopranome', 'attore')
    search_fields = ('nome','sopranome', 'attore')
    ordering = ("nome",)

