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
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="question_input_types_id",
    )


class Answers(models.Model):
    "Generated Model"
    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="answers_user_id",
    )
    answer = models.CharField(
        max_length=256,
    )
    question_option_id = models.ForeignKey(
        "questions.QuestionOptions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="answers_question_option_id",
    )


class Options(models.Model):
    "Generated Model"
    option_name = models.CharField(
        max_length=256,
    )


class QuestionOptions(models.Model):
    "Generated Model"
    question_id = models.ForeignKey(
        "questions.Question",
        on_delete=models.CASCADE,
        related_name="questionoptions_question_id",
    )
    option_id = models.ForeignKey(
        "questions.Options",
        on_delete=models.CASCADE,
        related_name="questionoptions_option_id",
    )


# Create your models here.
