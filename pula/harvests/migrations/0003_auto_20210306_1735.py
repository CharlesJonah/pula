# Generated by Django 3.1.7 on 2021-03-06 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('harvests', '0002_auto_20210306_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='farm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farm', to='harvests.farm'),
        ),
    ]
