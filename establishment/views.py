from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Establishment, Tip
from rest_framework.views import APIView
from .serializers import EstablishmentSerializer, TipSerializer


class EstablishmentCreateView(generics.CreateAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class EstablishmentListView(generics.ListAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class EstablishmentDetailView(generics.RetrieveAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class EstablishmentUpdateView(generics.UpdateAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class EstablishmentDeleteView(generics.DestroyAPIView):
    queryset = Establishment.objects.all()


class TipCreateView(generics.CreateAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer

    def perform_create(self, serializer):
        establishment_id = self.kwargs['pk']
        establishment = Establishment.objects.get(id=establishment_id)
        serializer.save(establishment=establishment)


@api_view(['GET', 'POST'])
def tip_payment_view(request, pk):
    establishment = get_object_or_404(Establishment, pk=pk)

    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            Tip.objects.create(establishment=establishment, amount=amount)
            return HttpResponse('Спасибо за ваш чаевые!', status=status.HTTP_201_CREATED)


class Waiter(APIView):
    def get(self, request):
        view = Waiter()
        result = view.get(request)
        return Response(result.data)


class Review(APIView):
    def get(self, request):
        view = Response()
        result = view.get(request)
        return Response(result.data)
