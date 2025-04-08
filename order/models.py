from django.db import models
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('delivered', 'Delivered'),
    ]
    DELIVERY_CHOICES = [
        ('home', 'Home Delivery'),
        ('center', 'Delivery Center'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    wilaya = models.CharField(max_length=100, default="01")  # Wilaya ID
    wilaya_name = models.CharField(max_length=100, default="Adrar")  # Wilaya name
    commune = models.CharField(max_length=100, default="1")  # Commune ID
    commune_name = models.CharField(max_length=100, default="Adrar")  # Commune name
    postal_code = models.CharField(max_length=10, default="00000")
    address = models.TextField()
    deliveryType = models.CharField(max_length=10, choices=DELIVERY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"

    def save(self, *args, **kwargs):
        # You can add logic here to automatically fill wilaya_name/commune_name
        super().save(*args, **kwargs)
