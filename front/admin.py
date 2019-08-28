from django.contrib import admin

from . import models


class FetAdmin(admin.ModelAdmin):
    list_display = ('name', )


class EntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'fet', 'time')
    list_filter = ('eround',)


class ProviderAdmin(admin.ModelAdmin):
    pass


class RoundAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Fet, FetAdmin)
admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Provider, ProviderAdmin)
admin.site.register(models.Round, RoundAdmin)
