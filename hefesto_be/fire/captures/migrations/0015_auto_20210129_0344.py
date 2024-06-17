# Generated by Django 3.1.2 on 2021-01-29 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captures', '0014_auto_20210128_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capture',
            name='calibr_image_name',
            field=models.CharField(default='1611891856.PNG', help_text='Camera calibration image name', max_length=255, null=True, verbose_name='camera calibration image name'),
        ),
    ]