from django.contrib import admin
from .models import Productions
# Register your models here.
@admin.register(Productions)
class ProductionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    list_display = ('nome','fase', 'uscita')
    # list_display = ('nome','sopranome', 'attore')
    # search_fields = ('nome','sopranome', 'attore')
    ordering = ("nome","uscita")

