# Generated by Django 4.2 on 2023-06-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_semso_semso_id_semso_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semso',
            name='id',
        ),
        migrations.AddField(
            model_name='semso',
            name='semso_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]