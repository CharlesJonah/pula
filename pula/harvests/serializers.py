from rest_framework import serializers

from .models import (
    Farm,
    Farmer,
    Harvest,
    Photo
)


class FarmSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True)
    modified_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Farm
        fields = ("id", "url", "location", "size", "crop",
                  "latitude", "longitude", "created_by", "modified_by", "created", "modified")
        extra_kwargs = {
            'created': {'read_only': True, 'required': False},
            'modified': {'read_only': True, 'required': False}
        }


class FarmerSerializer(serializers.HyperlinkedModelSerializer):

    created_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True)
    modified_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Farmer
        fields = ("id", "name", "url", "location", "latitude", "longitude",
                  "created_by", "modified_by", "created", "modified", "farm")
        extra_kwargs = {
            'created': {'read_only': True, 'required': False},
            'modified': {'read_only': True, 'required': False}
        }

    def validate(self, data):
        """
        Check if wet weight is greater than dry weight.
        """
        farm = Farm.objects.get(id=data['farm'].id)
        if (data['latitude'] != farm.latitude) and (data['longitude'] != farm.longitude):
            raise serializers.ValidationError(
                "The farmers geocordinates should be the same as those of the farm")
        return data


class HarvestSerializer(serializers.HyperlinkedModelSerializer):

    created_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True)
    modified_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Harvest
        fields = ("id", "url", "wet_weight", "dry_weight", "created_by",
                  "modified_by", "created", "modified", "farm")
        extra_kwargs = {
            'created': {'read_only': True, 'required': False},
            'modified': {'read_only': True, 'required': False}
        }

    def validate(self, data):
        """
        Check if wet weight is greater than dry weight.
        """
        harvest = Harvest.objects.filter(farm__id=data['farm'].id)
        if harvest:
            raise serializers.ValidationError(
                "A harvest is only limited to one farm")
        if data['dry_weight'] > data['wet_weight']:
            raise serializers.ValidationError(
                "Dry weight should be less that wet weight")
        return data


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    photo = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=False)
    )
    created_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True)
    modified_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Photo
        fields = ("id", "url", "photo", "created_by",
                  "modified_by", "created", "modified", "harvest")
        extra_kwargs = {
            'created': {'read_only': True, 'required': False},
            'modified': {'read_only': True, 'required': False}
        }

    def create(self, validated_data):
        photos = validated_data.pop('photo')
        for photo in photos:
            photo_obj = Photo.objects.create(photo=photo, **validated_data)
        return photo_obj

    def validate(self, data):
        """
        Check if wet weight is greater than dry weight.
        """
        photos = data['photo']
        if len(photos) < 3:
            raise serializers.ValidationError(
                "A minimum of 3 photos is required")
        return data
