"""Base URL classes for the app."""
from django.urls import path, include
from rest_framework import routers

from apps.business.views import BusinessModelAPIViewSet


router = routers.DefaultRouter()
router.register(r'data', BusinessModelAPIViewSet, basename='business-routers')

urlpatterns = [
    path('', include(router.urls)),
]