# Generated by Django 3.1.7 on 2021-03-05 11:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=50)),
                ('size', models.DecimalField(decimal_places=4, max_digits=10)),
                ('crop', models.CharField(max_length=50)),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('created_by', models.CharField(max_length=50)),
                ('modified_by', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]