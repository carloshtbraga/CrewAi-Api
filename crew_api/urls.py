from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import AgentViewSet, TaskViewSet, CrewViewSet, LlmViewSet, UserRegistrationView

router = routers.DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'crews', CrewViewSet)
router.register(r'llms', LlmViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Crew AI",
        default_version='v1',
        description="API que trabalha com CREWAI",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
