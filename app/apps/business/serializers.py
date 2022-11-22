"""Rest API Serializer classes of the app."""
from rest_framework.serializers import ModelSerializer

from apps.business.models import BusinessModel


class BusinessModelSerializer(ModelSerializer):
    """BusinessModel model's base serializer class."""

    class Meta:
        """Meta info of the class."""

        model = BusinessModel
        fields = '__all__'