# Generated by Django 3.2.7 on 2021-11-09 15:00

from django.db import migrations, models
import stubmaker_application.models


class Migration(migrations.Migration):

    dependencies = [
        ('stubmaker_application', '0002_stubdata_cpy'),
    ]

    operations = [
        migrations.AddField(
            model_name='stubdata',
            name='CL',
            field=models.ImageField(null=True, upload_to=stubmaker_application.models.path_and_rename),
        ),
    ]
