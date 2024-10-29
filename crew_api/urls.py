from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, TaskViewSet, CrewViewSet

router = DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'crews', CrewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
