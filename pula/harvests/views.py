from rest_framework import viewsets

from .models import Farm
from .serializers import AdminFarmSerializer


class FarmViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing farms.
    """
    queryset = Farm.objects.all()
    serializer_class = AdminFarmSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
