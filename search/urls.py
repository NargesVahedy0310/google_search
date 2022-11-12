from django.urls import path, include
from .views import *


urlpatterns = [
    path('search_box/', SearchBoxAPIView.as_view()),
    path('search_box/show/', SearchAPIView.as_view()),



    ]