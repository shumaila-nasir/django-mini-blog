# Generated by Django 4.1.1 on 2022-10-27 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='desceiption',
            new_name='description',
        ),
    ]