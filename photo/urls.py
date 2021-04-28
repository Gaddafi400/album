from django.urls import path
from photo.views import home

urlpatterns = [
    path('', home),
]
