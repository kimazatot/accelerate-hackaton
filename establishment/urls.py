from django.urls import path
from .views import (
    EstablishmentCreateView,
    EstablishmentListView,
    EstablishmentDetailView,
    EstablishmentUpdateView,
    EstablishmentDeleteView,
    TipCreateView,
    tip_payment_view,
)

urlpatterns = [
    path('establishments/', EstablishmentListView.as_view(), name='establishment-list'),
    path('establishments/create/', EstablishmentCreateView.as_view(), name='establishment-create'),
    path('establishments/<int:pk>/', EstablishmentDetailView.as_view(), name='establishment-detail'),
    path('establishments/<int:pk>/update/', EstablishmentUpdateView.as_view(), name='establishment-update'),
    path('establishments/<int:pk>/delete/', EstablishmentDeleteView.as_view(), name='establishment-delete'),
    path('establishments/<int:pk>/add_tip/', TipCreateView.as_view(), name='add-tip'),
    path('establishments/<int:pk>/tip_payment/', tip_payment_view, name='tip-payment'),

]
