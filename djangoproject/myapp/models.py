from django.db import models
from django.utils import timezone

class ChaiType(models.Model):
    CHAI_TYPES = [
        ('ML', 'Masala Chai'),
        ('EL', 'Elaichi Chai'),
        ('GR', 'Ginger Chai'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/chaitypes')

    chai_type = models.CharField(max_length=2, choices=CHAI_TYPES)
    price = models.TextField()  # text price (₹20, Free, etc.)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
