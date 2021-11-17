from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AnswersViewSet, InputTypesViewSet, QuestionViewSet

router = DefaultRouter()
router.register("inputtypes", InputTypesViewSet)
router.register("question", QuestionViewSet)
router.register("answers", AnswersViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
