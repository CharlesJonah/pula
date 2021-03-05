from rest_framework import serializers

from .models import Farm


class AdminFarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ["id", "location", "size", "crop",
                  "latitude", "longitude", "created_by", "modified_by", "created", "modified"]
        extra_kwargs = {'created_by': {'read_only': True,
                                       'default': serializers.CurrentUserDefault()},
                        'modified_by': {'read_only': True,
                                        'default': serializers.CurrentUserDefault()},
                        'created': {'read_only': True, 'required': False},
                        'modified': {'read_only': True, 'required': False}
                        }
