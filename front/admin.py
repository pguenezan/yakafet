from django.contrib import admin

from . import models


class FetAdmin(admin.ModelAdmin):
    list_display = ('name', )


class EntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'fet', 'time')

admin.site.register(models.Fet, FetAdmin)
admin.site.register(models.Entry, EntryAdmin)
