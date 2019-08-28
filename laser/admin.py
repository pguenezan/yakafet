from django.contrib import admin
from . import models

class LaserEntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.EntryLaser, LaserEntryAdmin)

