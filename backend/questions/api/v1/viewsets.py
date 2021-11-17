from rest_framework import authentication
from questions.models import Answers, InputTypes, Question
from .serializers import AnswersSerializer, InputTypesSerializer, QuestionSerializer
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
