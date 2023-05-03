from django.contrib import admin
from .models import Home
# Register your models here.
# admin.site.register(Home)

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields = {'slug': ('nome',)}
    # # list_display = ('nome','sopranome', 'attore')
    # # search_fields = ('nome','sopranome', 'attore')
    # ordering = ("nome",)

