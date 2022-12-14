# Generated by Django 4.1.2 on 2022-10-06 13:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        (
            "django_magicadmin",
            "0004_magiclink_used_at_alter_magiclink_secret_identifier",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="magiclink",
            name="secret_identifier",
            field=models.CharField(
                default=uuid.UUID("3d5764f1-e5dd-4456-94ea-c561207d5f72"),
                max_length=512,
            ),
        ),
    ]
