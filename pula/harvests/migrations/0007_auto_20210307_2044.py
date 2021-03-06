# Generated by Django 3.1.7 on 2021-03-07 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('harvests', '0006_harvest_photos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photo_url',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='harvest',
            name='photos',
        ),
        migrations.AlterField(
            model_name='photo',
            name='harvest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='harvest_photo', to='harvests.harvest'),
        ),
    ]
