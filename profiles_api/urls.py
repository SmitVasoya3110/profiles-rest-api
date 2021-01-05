from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HelloApiView, HelloViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename = 'hello-viewset')
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('hello-api', HelloApiView.as_view(), name='hello-api'),
    path('', include(router.urls)),    
]