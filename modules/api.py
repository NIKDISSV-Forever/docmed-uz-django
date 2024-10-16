from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from modules.models import *
from modules.serializers import *

__all__ = ('ModuleProgress', 'ModuleProgressViewSet', 'TimecodeViewSet', 'SponsorViewSet')


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # the permissions need to be clarified in the future


class ModuleProgressViewSet(viewsets.ModelViewSet):
    queryset = ModuleProgress.objects.all()
    serializer_class = ModuleProgressSerializer
    permission_classes = [IsAuthenticated]


class TimecodeViewSet(viewsets.ModelViewSet):
    queryset = Timecode.objects.all()
    serializer_class = TimecodeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
