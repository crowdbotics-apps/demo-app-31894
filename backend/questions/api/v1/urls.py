from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    AnswersViewSet,
    InputTypesViewSet,
    OptionsViewSet,
    QuestionViewSet,
    QuestionOptionsViewSet,
)

router = DefaultRouter()
router.register("inputtypes", InputTypesViewSet)
router.register("question", QuestionViewSet)
router.register("answers", AnswersViewSet)
router.register("options", OptionsViewSet)
router.register("questionoptions", QuestionOptionsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
