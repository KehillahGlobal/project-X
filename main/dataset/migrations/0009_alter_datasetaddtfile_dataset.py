# Generated by Django 4.2.3 on 2023-08-01 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0008_remove_dataset_dataset_addt_files_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetaddtfile',
            name='dataset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='dataset.dataset'),
        ),
    ]
