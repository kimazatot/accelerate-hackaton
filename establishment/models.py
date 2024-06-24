from django.db import models
from uuid import uuid4
from qr_app.utils import generate_qr_code


class Establishment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    owner_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr_data = f"Address: {self.address}, Owner: {self.owner_name}, Phone: {self.phone_number}"
        qr_code_file = generate_qr_code(qr_data)
        self.qr_code.save(f"{self.owner_name}_qr.png", qr_code_file, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Establishment - {self.owner_name}"


