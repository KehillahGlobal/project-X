# Generated by Django 4.2.3 on 2023-08-12 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0017_file_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='org',
            new_name='owner_org',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='user',
            new_name='owner_user',
        ),
    ]
