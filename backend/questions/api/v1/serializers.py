from rest_framework import serializers
from questions.models import Answers, InputTypes, Options, Question, QuestionOptions


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


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = "__all__"


class QuestionOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOptions
        fields = "__all__"
