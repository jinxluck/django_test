# Generated by Django 2.2.5 on 2019-11-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_poc', '0003_testdatabase_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdatabase',
            name='NODELETE',
            field=models.BooleanField(default=False),
        ),
    ]
