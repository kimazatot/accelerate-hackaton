"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from qr_app import views as qr_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/qr_app/waiters/', qr_views.WaiterListCreateAPIView.as_view(), name='waiter-list-create'),
    path('api/v1/qr_app/waiters/<int:pk>/', qr_views.WaiterDetailAPIView.as_view(), name='waiter-detail'),

    path('api/v1/qr_app/waiters/<int:waiter_id>/reviews/', qr_views.ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('api/v1/qr_app/waiters/<int:waiter_id>/reviews/<int:pk>/', qr_views.ReviewDetailAPIView.as_view(), name='review-detail'),

    path('api/v1/qr_app/payments/', qr_views.PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path('api/v1/qr_app/payments/<int:pk>/', qr_views.PaymentDetailAPIView.as_view(), name='payment-detail'),
]
