# establishments/urls.py
from django.urls import path
from .views import EstablishmentListCreateAPIView, EstablishmentDetailAPIView

urlpatterns = [
    path('establishments/', EstablishmentListCreateAPIView.as_view(), name='establishment-list'),
    path('establishments/<uuid:pk>/', EstablishmentDetailAPIView.as_view(), name='establishment-detail'),
]
