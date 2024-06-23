from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Waiter, Review, Payment, Establishment, RegistrationRequest
from .serializers import (
    WaiterSerializer, ReviewSerializer, PaymentSerializer, EstablishmentSerializer,
    RegistrationRequestSerializer
)
import qrcode


@require_http_methods(["POST", "GET"])
def submit_registration_request(request):
    if request.method == 'POST':
        establishment_name = request.POST.get('establishment_name')
        contact_email = request.POST.get('contact_email')

        if not establishment_name or not contact_email:
            return HttpResponse('Некорректные данные для заявки на регистрацию.', status=status.HTTP_400_BAD_REQUEST)

        registration_request = RegistrationRequest.objects.create(
            establishment_name=establishment_name,
            contact_email=contact_email,
            status='pending'
        )

        return HttpResponse('Заявка на регистрацию отправлена.')
    else:
        return render(request, 'submit_registration_request.html')


def approve_registration_request(request, request_id):
    try:
        registration_request = RegistrationRequest.objects.get(pk=request_id)
    except RegistrationRequest.DoesNotExist:
        return HttpResponse(f'Заявка с id {request_id} не найдена.', status=status.HTTP_404_NOT_FOUND)

    registration_request.status = 'approved'
    registration_request.save()

    qr_filename = f'qr_{registration_request.id}.png'
    generate_qr_code(registration_request.establishment_name, qr_filename)

    return HttpResponse(f'Заявка одобрена. QR-код сохранен как {qr_filename}')


def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)


class WaiterListCreateAPIView(generics.ListCreateAPIView):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        waiter = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        waiter_id = self.kwargs.get('waiter_id')
        return Review.objects.filter(waiter_id=waiter_id)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PaymentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


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
