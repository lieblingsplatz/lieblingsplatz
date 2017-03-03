from django.contrib import admin
from map.models import Kita, Phone


class KitaAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Kita, KitaAdmin)
admin.site.register(Phone)
