from rest_framework.serializers import ModelSerializer

from startPrintLabels.models import SKU


class SKU_Serializer(ModelSerializer):
    class Meta:
        model = SKU
        fields = ['gtin', 'name']
