from django.urls import path

from .views import ScholeDeviceRegistrationView

urlpatterns = [
    path("v1/school-registration", ScholeDeviceRegistrationView.as_view(), name="school-registration"),
]
