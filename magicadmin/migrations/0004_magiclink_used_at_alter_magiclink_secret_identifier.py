# Generated by Django 4.1.2 on 2022-10-05 16:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("magicadmin", "0003_alter_magiclink_expires_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="magiclink",
            name="used_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="magiclink",
            name="secret_identifier",
            field=models.CharField(
                default=uuid.UUID("c14bec12-56dc-4795-8891-a55b31f33de8"),
                max_length=512,
            ),
        ),
    ]
