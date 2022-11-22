"""Main API view classes of the app."""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.business.serializers import BusinessModelSerializer


# Create your views here.
class BusinessModelAPIViewSet(ModelViewSet):
    """BusinessModel model class base API viewset class."""

    serializer_class = BusinessModelSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]
