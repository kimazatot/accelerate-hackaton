from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Establishment, Tip
from .serializers import EstablishmentSerializer, TipSerializer


class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer

    @action(detail=True, methods=['post'])
    def add_tip(self, request, pk=None):
        establishment = self.get_object()
        serializer = TipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(establishment=establishment)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TipViewSet(viewsets.ModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
