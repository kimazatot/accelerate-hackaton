from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.conf import settings
from io import BytesIO
import qrcode
from PIL import Image as PilImage
from uuid import uuid4


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    committed_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    @property
    def fragment(self):
        return f"{self.amount}_{self.id}"

    @property
    def qr_url(self):
        return reverse('payment-qr', args=[self.id.hex])

    @property
    def checkout_url(self):
        return reverse('payment-detail', args=[self.id.hex])

    def generate_qr_code(self):
        data = f"{settings.QR_BASE_URL}#{self.fragment}"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image()

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)

        return buffer

    def __str__(self):
        return f"Payment #{self.id}"


class Waiter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review #{self.id} for {self.waiter.name}"


class Establishment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    owner_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    @property
    def qr_code_url(self):
        return reverse('establishment-qr', args=[str(self.id)])

    def generate_qr_code(self):
        data = f"Owner: {self.owner_name}\nPhone: {self.phone_number}\nAddress: {self.address}"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save the generated QR code in a buffer
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)

        return buffer

    def __str__(self):
        return f"Establishment - {self.owner_name}"



