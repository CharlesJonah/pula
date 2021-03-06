# Generated by Django 3.1.7 on 2021-03-06 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('harvests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='photo_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='farm',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farm_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='farm',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farm_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farmer_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='farmer_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='harvest_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='harvest_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Photot',
        ),
        migrations.AddField(
            model_name='photo',
            name='harvest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvests.harvest'),
        ),
        migrations.AddField(
            model_name='photo',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='photo_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
