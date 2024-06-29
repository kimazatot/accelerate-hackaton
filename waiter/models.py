from django.db import models
from establishment.models import Establishment
from django.core.validators import MinValueValidator, MaxValueValidator


class Waiter(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    photo = models.ImageField(upload_to='waiter_photos/', null=True, blank=True)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, related_name='waiters')

    def __str__(self):
        return f"{self.name} from {self.establishment.name}"


class Review(models.Model):
    waiter = models.ForeignKey('Waiter', on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review #{self.id} for {self.waiter.name}"
