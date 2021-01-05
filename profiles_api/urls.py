from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HelloApiView, HelloViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename = 'hello-viewset')

urlpatterns = [
    path('hello-api', HelloApiView.as_view(), name='hello-api'),
    path('', include(router.urls)),    
]