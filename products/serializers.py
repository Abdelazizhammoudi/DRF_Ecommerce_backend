from rest_framework import serializers
from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'image_url']
        read_only_fields = ['id']

    def get_image_url(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=100000,
            allow_empty_file=False,
            use_url=False
        ),
        write_only=True,
        required=False
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 
        'images', 'uploaded_images', 'available_stock', 'quantity']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'price': {'required': True},
        }

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        product = Product.objects.create(**validated_data)
        
        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)
            
        return product

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        
        # Update the product instance
        instance = super().update(instance, validated_data)
        
        # Add new images
        for image in uploaded_images:
            ProductImage.objects.create(product=instance, image=image)
        
        # Return the updated instance
        return instance

