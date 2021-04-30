from django.urls import path
from photo.views import HomeView, StudentDetailView

urlpatterns = [
    # path('', home),
    path('', HomeView.as_view(), name="home"),
    path('student/<int:pk>/', StudentDetailView.as_view(), name="student")
]
