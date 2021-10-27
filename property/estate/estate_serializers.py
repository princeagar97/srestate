from rest_framework import serializers
from property.models import Estate, EstateStatus, EstateType,photos,City,Apartment






class EstateSerializer(serializers.ModelSerializer):
    Images  = serializers.ImageField()

    def create(self,validate_data):
        return Estate.objects.create(**validate_data)

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


class ImageSerializer(serializers.ModelSerializer):

    def create(self,validate_data):
        return photos.objects.create(**validate_data)

    class Meta:
        model = photos
        fields = '__all__'