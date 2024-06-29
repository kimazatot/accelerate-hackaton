from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from .models import Payment, QRCode, RegistrationRequest
from .serializers import (PaymentSerializer, QRCodeSerializer,
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
    registration_request = get_object_or_404(RegistrationRequest, pk=request_id)

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


class QRCodeViewSet(viewsets.ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer