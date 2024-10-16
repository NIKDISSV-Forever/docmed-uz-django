from django.contrib import admin

from courses.models import *

__all__ = ('TagAdmin', 'SpeakerAdmin', 'DrugAdmin', 'AttachAdmin', 'CourseAdmin')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    pass


@admin.register(Attach)
class AttachAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
