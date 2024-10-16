import textwrap

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from docmed.utils import get_timestamp_upload_to

__all__ = ('Sponsor', 'Module', 'ModuleProgress', 'Timecode')


class ModuleProgress(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'module'], name='unique_user_module')
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    video_watched = models.BooleanField(default=False)
    files_downloaded = models.BooleanField(default=False)
    test_passed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.module.title} progress'


class Sponsor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Timecode(models.Model):
    module = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='timecodes')
    time = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f"{self.time} - {textwrap.shorten(self.description, 50, placeholder='...')}"


class Module(models.Model):
    title = models.CharField(max_length=255)
    video = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to=get_timestamp_upload_to)
    description = models.TextField()
    speakers = models.ManyToManyField('courses.Speaker', related_name='modules_speakers', blank=True)
    drugs = models.ManyToManyField('courses.Drug', related_name='modules_drugs', blank=True)
    sponsor = models.ForeignKey('Sponsor', on_delete=models.SET_NULL, null=True, blank=True)
    attaches = models.ManyToManyField('courses.Attach', related_name='modules_attaches', blank=True)
    tags = models.ManyToManyField('courses.Tag', related_name='modules_tags', blank=True)
    disclaimer = models.TextField(blank=True, null=True)
    part_of_course = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def clean(self):
        if not (self.video or self.image):
            raise ValidationError('Must provide either a video or a image')
        super().clean()
