# Generated by Django 3.1.2 on 2021-01-29 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detections', '0004_auto_20210129_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='file_path',
            field=models.TextField(null=True, verbose_name='detection file path'),
        ),
    ]