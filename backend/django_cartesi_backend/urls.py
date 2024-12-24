from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("users.urls")),
    #  JWT token generation paths
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Bridge and school device registration paths
    path("api/", include("bridge.urls"), name="bridge"),
    path("api/", include("iot_registration.urls"), name="iot-registration"),
]
