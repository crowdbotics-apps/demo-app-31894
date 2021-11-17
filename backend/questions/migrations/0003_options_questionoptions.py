# Generated by Django 2.2.24 on 2021-11-17 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0002_answers"),
    ]

    operations = [
        migrations.CreateModel(
            name="Options",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("option_name", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="QuestionOptions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "option_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questionoptions_option_id",
                        to="questions.Options",
                    ),
                ),
                (
                    "question_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questionoptions_question_id",
                        to="questions.Question",
                    ),
                ),
            ],
        ),
    ]
