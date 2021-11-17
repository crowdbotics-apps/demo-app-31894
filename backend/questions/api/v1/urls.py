from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import InputTypesViewSet, QuestionViewSet

router = DefaultRouter()
router.register("inputtypes", InputTypesViewSet)
router.register("question", QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
