import uuid
from django.db import models
from django.contrib.auth.models import User


class Farm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.CharField(max_length=50, unique=True)
    size = models.DecimalField(max_digits=10, decimal_places=4)
    crop = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    created_by = models.ForeignKey(
        to=User, related_name='farm_created_by', on_delete=models.DO_NOTHING)
    modified_by = models.ForeignKey(
        to=User, related_name='farm_modified_by', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location


class Farmer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
    )
    created_by = models.ForeignKey(
        to=User, related_name='farmer_created_by', on_delete=models.DO_NOTHING)
    modified_by = models.ForeignKey(
        to=User, related_name='farmer_modified_by', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Harvest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wet_weight = models.DecimalField(max_digits=10, decimal_places=4)
    dry_weight = models.DecimalField(max_digits=10, decimal_places=4)
    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
    )
    created_by = models.ForeignKey(
        to=User, related_name='harvest_created_by', on_delete=models.DO_NOTHING)
    modified_by = models.ForeignKey(
        to=User, related_name='harvest_modified_by', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to='uploads/')
    harvest = models.ForeignKey(
        Harvest,
        related_name='harvest_photo',
        on_delete=models.CASCADE,
    )
    created_by = models.ForeignKey(
        to=User, related_name='photo_created_by', on_delete=models.DO_NOTHING)
    modified_by = models.ForeignKey(
        to=User, related_name='photo_modified_by', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
