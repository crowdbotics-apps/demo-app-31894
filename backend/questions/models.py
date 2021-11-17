from django.conf import settings
from django.db import models


class InputTypes(models.Model):
    "Generated Model"
    input_type_name = models.CharField(
        max_length=256,
    )


class Question(models.Model):
    "Generated Model"
    question_name = models.CharField(
        max_length=256,
    )
    input_types_id = models.ForeignKey(
        "questions.InputTypes",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="question_input_types_id",
    )


# Create your models here.
