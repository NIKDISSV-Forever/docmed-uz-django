from django.contrib import admin

from modules.models import *

__all__ = ('SponsorAdmin', 'ModuleAdmin', 'ModuleProgressAdmin', 'TimecodeAdmin')


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass


@admin.register(ModuleProgress)
class ModuleProgressAdmin(admin.ModelAdmin):
    pass


@admin.register(Timecode)
class TimecodeAdmin(admin.ModelAdmin):
    pass


class TimecodeInline(admin.TabularInline):
    model = Timecode
    extra = 1


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = (TimecodeInline,)
