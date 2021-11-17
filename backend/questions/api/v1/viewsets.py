from rest_framework import authentication
from questions.models import Answers, InputTypes, Options, Question, QuestionOptions
from .serializers import (
    AnswersSerializer,
    InputTypesSerializer,
    OptionsSerializer,
    QuestionSerializer,
    QuestionOptionsSerializer,
)
from rest_framework import viewsets


class InputTypesViewSet(viewsets.ModelViewSet):
    serializer_class = InputTypesSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = InputTypes.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Question.objects.all()


class AnswersViewSet(viewsets.ModelViewSet):
    serializer_class = AnswersSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Answers.objects.all()


class OptionsViewSet(viewsets.ModelViewSet):
    serializer_class = OptionsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Options.objects.all()


class QuestionOptionsViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionOptionsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = QuestionOptions.objects.all()
