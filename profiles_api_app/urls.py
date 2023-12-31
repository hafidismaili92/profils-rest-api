from django.urls import path, include
from profiles_api_app import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('test-viewset',views.Testapiviewsets, basename='test-viewset')
router.register('profile',views.UserProfilViewSet)
router.register('feed',views.UserProfilFeedViewSet)
urlpatterns = [
    path('testApiView/', views.TestApiView.as_view()),
    path('login',views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]