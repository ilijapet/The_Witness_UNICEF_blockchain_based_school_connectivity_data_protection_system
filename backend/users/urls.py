from django.urls import path

from .views import (
    BlacklistTokenUpdateView,
    CustomUserCreate,
    PasswordRestRequestView,
    ResetPasswordAPIView,
    UserProfileView,
)

app_name = "users"

urlpatterns = [
    path("register/", CustomUserCreate.as_view(), name="create_user"),
    path("userStatus/", UserProfileView.as_view(), name="user_profile"),
    path(
        "resetpassword/",
        PasswordRestRequestView.as_view(),
        name="request_reset_password",
    ),
    path(
        "resetpassword/<str:encoded_pk>/<str:token>/",
        ResetPasswordAPIView.as_view(),
        name="reset-password",
    ),
    path("logout/blacklist/", BlacklistTokenUpdateView.as_view(), name="blacklist"),
]
