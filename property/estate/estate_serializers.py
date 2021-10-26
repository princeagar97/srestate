from rest_framework import serializers
from property.models import Estate, EstateStatus, EstateType






class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        exclude = ["is_deleted"]



class EstateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateStatus
        exclude = ["is_deleted"]


class EstateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateType
        exclude = ["is_deleted"]
