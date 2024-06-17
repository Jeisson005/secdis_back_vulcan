# Generated by Django 3.1.2 on 2020-10-21 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='file_name',
            field=models.CharField(max_length=100, null=True, verbose_name='detection file name'),
        ),
        migrations.AlterField(
            model_name='detection',
            name='file_path',
            field=models.FileField(null=True, upload_to='', verbose_name='detection file path'),
        ),
        migrations.AlterField(
            model_name='detection',
            name='processing_date',
            field=models.DateTimeField(null=True, verbose_name='processing date'),
        ),
    ]
