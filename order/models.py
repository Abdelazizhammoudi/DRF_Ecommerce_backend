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
    address = models.TextField()
    deliveryType = models.CharField(max_length=10, choices=DELIVERY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"