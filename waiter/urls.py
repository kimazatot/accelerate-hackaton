from django.urls import path
from .views import WaiterListCreate, WaiterRetrieveUpdateDestroy, ReviewListCreate, ReviewRetrieveUpdateDestroy

urlpatterns = [
    path('waiters/', WaiterListCreate.as_view(), name='waiter-list-create'),
    path('waiters/<int:pk>/', WaiterRetrieveUpdateDestroy.as_view(), name='waiter-retrieve-update-destroy'),
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroy.as_view(), name='review-retrieve-update-destroy'),
]
