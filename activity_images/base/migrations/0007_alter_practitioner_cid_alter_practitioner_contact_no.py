# Generated by Django 4.2 on 2023-06-07 19:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_financialstatement_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practitioner',
            name='cid',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(11)]),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='contact_no',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]