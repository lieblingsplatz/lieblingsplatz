from django.contrib import admin

from map.models import Kita

class KitaAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Kita, KitaAdmin)