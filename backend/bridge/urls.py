from django.urls import path

from .views import BridgeView

urlpatterns = [
    path("v1/bridge", BridgeView.as_view(), name="bridge"),
]
