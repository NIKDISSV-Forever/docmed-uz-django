from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from courses.serializers import *


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AttachViewSet(viewsets.ModelViewSet):
    queryset = Attach.objects.all()
    serializer_class = AttachSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
