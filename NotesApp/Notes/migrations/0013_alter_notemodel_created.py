# Generated by Django 3.2.8 on 2021-10-27 17:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0012_alter_notemodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 27, 17, 15, 43, 389961, tzinfo=utc)),
        ),
    ]
