# Generated by Django 4.2.2 on 2023-08-16 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0020_alter_user_email"),
        ("dataset", "0018_rename_org_file_owner_org_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="user", new_name="owner_user",
        ),
        migrations.RenameField(
            model_name="like", old_name="user", new_name="owner_user",
        ),
        migrations.AddField(
            model_name="comment",
            name="status",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="dataset",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="dataset",
            name="is_archived",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="dataset",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="Bookmark",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="dataset.dataset",
                    ),
                ),
                (
                    "owner_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="user.user"
                    ),
                ),
            ],
        ),
    ]
