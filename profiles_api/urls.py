from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HelloApiView, HelloViewSet, UserProfileViewSet, UserLoginApiView, UserProfileFeedView

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename = 'hello-viewset')
router.register('profile', UserProfileViewSet),
router.register('feed', UserProfileFeedView)

urlpatterns = [
    path('hello-api', HelloApiView.as_view(), name='hello-api'),
    path('login', UserLoginApiView.as_view()),
    path('', include(router.urls)),    
]