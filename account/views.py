from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Establishment
from .serializers import UserRegistrationSerializer, EstablishmentSerializer

User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'email': user.email, 'name': user.name}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstablishmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer

    def perform_create(self, serializer):
        owner = self.request.user
        serializer.save(owner=owner, pending_approval=True)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'detail': 'Аутентификация не пройдена.'}, status=status.HTTP_401_UNAUTHORIZED)
        return super().post(request, *args, **kwargs)
