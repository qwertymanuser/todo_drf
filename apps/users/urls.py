from django.urls import path 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserAPIViewSet

router = DefaultRouter()
router.register('users', UserAPIViewSet, "api_users")

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls