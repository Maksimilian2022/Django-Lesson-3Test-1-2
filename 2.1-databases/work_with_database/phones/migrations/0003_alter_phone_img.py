# Generated by Django 4.0.6 on 2022-12-24 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='img',
            field=models.CharField(max_length=200),
        ),
    ]