from django.urls import path, include
from rest_framework.routers import DefaultRouter

from App import views

# router = DefaultRouter()
# router.register(prefix="viewsets", viewset=views.DoctorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
