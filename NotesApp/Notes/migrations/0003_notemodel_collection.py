# Generated by Django 3.2.8 on 2021-10-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0002_auto_20211024_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='notemodel',
            name='collection',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]