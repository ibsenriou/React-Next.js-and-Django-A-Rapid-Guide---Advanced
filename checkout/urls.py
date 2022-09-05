from django.urls import path

from .views import LinkAPIView

urlpatterns = [
    path('links/<str:code>', LinkAPIView.as_view())
]
