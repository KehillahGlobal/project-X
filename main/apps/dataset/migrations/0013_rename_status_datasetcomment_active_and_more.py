# Generated by Django 4.2.3 on 2023-10-06 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0012_rename_dataset_file_dataset_datasetfile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasetcomment',
            old_name='status',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='datasetlike',
            old_name='status',
            new_name='active',
        ),
    ]
