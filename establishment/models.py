from django.db import models
from qr_app.utils import generate_qr_code


class Establishment(models.Model):
    name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    owner_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)

        qr_data = self.get_tip_payment_url()
        qr_code_file = generate_qr_code(qr_data)
        self.qr_code.save(f"{self.name}_qr.png", qr_code_file, save=False)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('establishment-detail', kwargs={'pk': self.pk})

    def get_tip_payment_url(self):
        from django.urls import reverse
        return reverse('tip-payment', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Tip(models.Model):
    establishment = models.ForeignKey(Establishment, related_name='tips', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} - {self.establishment.name}"
