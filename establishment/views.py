from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Establishment
from .serializers import EstablishmentSerializer


class EstablishmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        establishment = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EstablishmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
