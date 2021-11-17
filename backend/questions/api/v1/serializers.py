from rest_framework import serializers
from questions.models import InputTypes, Question


class InputTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputTypes
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
