from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'product', 'firstName', 'lastName', 
            'phone', 'wilaya', 'wilaya_name', 'commune', 'commune_name',
            'postal_code', 'address', 'deliveryType', 'status', 'created_at',
            'quantity', 'total_price'
        ]
        extra_kwargs = {
            'product': {'required': True},
            'firstName': {'required': True},
            'lastName': {'required': True},
            'phone': {'required': True},
            'wilaya': {'required': True},
            'commune': {'required': True},
            'address': {'required': True},
            'deliveryType': {'required': True},
            'status': {'read_only': False},
            # These fields are optional, as their values will now come from the frontend
            'wilaya_name': {'required': False},
            'commune_name': {'required': False},
            'postal_code': {'required': False},
            'created_at': {'read_only': True},
            'quantity': {'required': False},
            'total_price': {'required': False}
        }

    def validate_deliveryType(self, value):
        if value not in [choice[0] for choice in Order.DELIVERY_CHOICES]:
            raise serializers.ValidationError("Invalid delivery type selected")
        return value.lower()

    def validate_phone(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Invalid phone number format")
        return value

    def validate_wilaya(self, value):
        if not value:
            raise serializers.ValidationError("Wilaya is required")
        return value

    def validate_commune(self, value):
        if not value:
            raise serializers.ValidationError("Commune is required")
        return value

    def create(self, validated_data):
        # By not removing the location fields, we preserve the user provided wilaya_name,
        # commune_name and postal_code values.
        return super().create(validated_data)
