from rest_framework import serializers

from modules.models import *

__all__ = ('ModuleProgressSerializer', 'ModuleSerializer', 'TimecodeSerializer', 'SponsorSerializer')


class ModuleProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleProgress
        fields = '__all__'


class TimecodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timecode
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    timecodes = TimecodeSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = '__all__'


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'
