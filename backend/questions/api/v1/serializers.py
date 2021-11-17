from rest_framework import serializers
from questions.models import Answers, InputTypes, Question


class InputTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputTypes
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"
