from rest_framework import generics
from .models import Waiter, Review
from .serializers import WaiterSerializer, ReviewSerializer


class WaiterListCreate(generics.ListCreateAPIView):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer


class WaiterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer


class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer