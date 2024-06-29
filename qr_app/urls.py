from django.urls import path
from .views import (
    PaymentListCreateAPIView, PaymentDetailAPIView,
    submit_registration_request, approve_registration_request, QRCodeViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'qrcodes', QRCodeViewSet)

urlpatterns = [

    path('payments/', PaymentListCreateAPIView.as_view(), name='payment-list'),
    path('payments/<uuid:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),

    path('submit-registration/', submit_registration_request, name='submit-registration'),
    path('approve-registration/<int:request_id>/', approve_registration_request, name='approve-registration'),
]
