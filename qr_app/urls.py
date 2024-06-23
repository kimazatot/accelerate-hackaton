from django.urls import path
from .views import (
    WaiterListCreateAPIView, WaiterDetailAPIView,
    ReviewListCreateAPIView, ReviewDetailAPIView,
    PaymentListCreateAPIView, PaymentDetailAPIView,
    EstablishmentListCreateAPIView, EstablishmentDetailAPIView,
    submit_registration_request, approve_registration_request
)

urlpatterns = [
    path('waiters/', WaiterListCreateAPIView.as_view(), name='waiter-list'),
    path('waiters/<int:pk>/', WaiterDetailAPIView.as_view(), name='waiter-detail'),

    path('waiters/<int:waiter_id>/reviews/', ReviewListCreateAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),

    path('payments/', PaymentListCreateAPIView.as_view(), name='payment-list'),
    path('payments/<uuid:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),

    path('establishments/', EstablishmentListCreateAPIView.as_view(), name='establishment-list'),
    path('establishments/<uuid:pk>/', EstablishmentDetailAPIView.as_view(), name='establishment-detail'),

    path('submit-registration/', submit_registration_request, name='submit-registration'),
    path('approve-registration/<int:request_id>/', approve_registration_request, name='approve-registration'),
]
