# Generated by Django 4.2 on 2023-05-22 15:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_executivemember_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='activity_images/'),
        ),
        migrations.AlterField(
            model_name='financialstatement',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='financial_statements/'),
        ),
    ]