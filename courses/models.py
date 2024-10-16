from django.contrib.contenttypes.models import ContentType
from django.db import models

__all__ = ('Tag', 'Speaker', 'Drug', 'Course', 'Attach')

from docmed.utils import get_timestamp_upload_to


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Speaker(models.Model):
    photo = models.ImageField(upload_to=get_timestamp_upload_to, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    courses = models.ManyToManyField('Course', related_name='speakers_courses')

    def __str__(self):
        return self.full_name


class Drug(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_timestamp_upload_to, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='drugs_tags', blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_timestamp_upload_to, blank=True,
                              null=True)  # Используем функцию для имени файла
    description = models.TextField()
    module_count = models.PositiveIntegerField()
    modules = models.ManyToManyField('modules.Module', related_name='courses_modules')
    speakers = models.ManyToManyField('Speaker', related_name='courses_speakers', blank=True)
    attaches = models.ManyToManyField('Attach', related_name='courses_attaches', blank=True)
    drugs = models.ManyToManyField('Drug', related_name='courses_drugs', blank=True)
    tags = models.ManyToManyField('Tag', related_name='courses_tags', blank=True)
    disclaimer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Attach(models.Model):
    class Meta:
        verbose_name_plural = 'Attachments'

    file = models.FileField(upload_to=get_timestamp_upload_to)

    def __str__(self):
        return self.file.name
