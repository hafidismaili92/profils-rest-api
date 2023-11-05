from django.urls import path
from profiles_api_app import views
urlpatterns = [
    path('testApiView/', views.TestApiView.as_view()),
]