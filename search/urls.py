from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('Search', SearchView, basename='Search')
router.register('SearchBox', SearchBoxView, basename='Search Box')

urlpatterns = [
    path("", include(router.urls)),


    ]