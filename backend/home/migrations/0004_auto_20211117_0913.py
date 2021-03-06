# Generated by Django 2.2.24 on 2021-11-17 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0003_userprofile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="temp",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="userid",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userprofile_userid",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
