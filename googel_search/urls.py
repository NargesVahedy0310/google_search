from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('value_search', A, basename='searching')
router.register('google_search', B, basename='search')




urlpatterns = [
    path('google_search/show/', SearchListView.as_view()),
    path("", include(router.urls)),

]