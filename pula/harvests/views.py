from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
    JSONParser
)

from .models import (
    Farm,
    Farmer,
    Harvest,
    Photo
)
from .serializers import (
    FarmSerializer,
    FarmerSerializer,
    HarvestSerializer,
    PhotoSerializer,
)


class FarmViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing farms.
    """
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

    def perform_create(self, serializer):
        request = serializer.context["request"]
        serializer.save(created_by=request.user, modified_by=request.user)

    def perform_update(self, serializer):
        request = serializer.context["request"]
        instance = get_object_or_404(Farm, id=self.kwargs['pk'])
        serializer.save(created_by=instance.created_by,
                        modified_by=request.user)


class FarmerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing farmers.
    """
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

    def perform_create(self, serializer):
        request = serializer.context["request"]
        serializer.save(created_by=request.user, modified_by=request.user)

    def perform_update(self, serializer):
        request = serializer.context["request"]
        instance = get_object_or_404(Farmer, id=self.kwargs['pk'])
        serializer.save(created_by=instance.created_by,
                        modified_by=request.user)


class HarvestViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing harvests.
    """
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer

    def perform_create(self, serializer):
        request = serializer.context["request"]
        serializer.save(created_by=request.user, modified_by=request.user)

    def perform_update(self, serializer):
        request = serializer.context["request"]
        instance = get_object_or_404(Harvest, id=self.kwargs['pk'])
        serializer.save(created_by=instance.created_by,
                        modified_by=request.user)


class PhotoViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing photos.
    """
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def perform_create(self, serializer):
        request = serializer.context["request"]
        serializer.save(created_by=request.user, modified_by=request.user)

    def perform_update(self, serializer):
        request = serializer.context["request"]
        instance = get_object_or_404(Photo, id=self.kwargs['pk'])
        serializer.save(created_by=instance.created_by,
                        modified_by=request.user)
