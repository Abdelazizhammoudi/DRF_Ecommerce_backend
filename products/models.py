from django.db import models

class Product(models.Model):
    # Product model with a relationship to ProductImage.
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url  # Keep the leading slash
        return None