from rest_framework import serializers

from courses.models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class AttachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attach
        fields = '__all__'
