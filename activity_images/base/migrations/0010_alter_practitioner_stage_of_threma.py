# Generated by Django 4.2 on 2023-06-07 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_practitioner_bob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practitioner',
            name='stage_of_threma',
            field=models.CharField(blank=True, choices=[('Chapdro', 'Chapdro'), ('Semkey', 'Semkey'), ('Mendray', 'Mendray'), ('Yoenla Dinpa', 'Yoenla Dinpa'), ('Ku Sum Domdey', 'Ku Sum Domdey'), ('Lami Nyelijor', 'Lami Nyelijor')], max_length=255, null=True),
        ),
    ]
