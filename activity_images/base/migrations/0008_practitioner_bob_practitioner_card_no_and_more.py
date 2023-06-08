# Generated by Django 4.2 on 2023-06-07 19:51

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_practitioner_cid_alter_practitioner_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='practitioner',
            name='bob',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='practitioner',
            name='card_no',
            field=models.CharField(default=12, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='practitioner',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='profile-icon-login-head-icon-vector_teheof.jpg', max_length=255, verbose_name='profile_pics'),
        ),
    ]
