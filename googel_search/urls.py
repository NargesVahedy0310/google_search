from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('search', GoogelSearchAPI, basename='searching')





urlpatterns = [
    path('search/show/', ValueSearchListView.as_view()),
    path("", include(router.urls)),

]