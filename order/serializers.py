from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'product', 'firstName', 'lastName', 
            'phone', 'address', 'deliveryType', 'status', 'created_at'
        ]
        extra_kwargs = {
            'product': {'required': True},
            'firstName': {'required': True},
            'lastName': {'required': True},
            'phone': {'required': True},
            'address': {'required': True},
            'deliveryType': {'required': True},
            'status': {'read_only': False},  # Allow status updates
        }

    def validate_deliveryType(self, value):
        if value not in [choice[0] for choice in Order.DELIVERY_CHOICES]:
            raise serializers.ValidationError("Invalid delivery type selected")
        return value.lower()

    def validate_phone(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Invalid phone number format")
        return value