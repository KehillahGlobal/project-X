# Generated by Django 4.2.3 on 2023-07-23 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_about_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
