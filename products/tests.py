from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Product, ProductImage
import requests

# # class ProductImageUpdateTest(TestCase):
# #     def setUp(self):
# #         self.client = Client()
# #         self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.00)
# #         self.product_image = ProductImage.objects.create(product=self.product, image='test_image.jpg')

# #     def test_update_product_image(self):
# #         with open('test_image.jpg', 'rb') as image:
# #             response = self.client.put(
# #                 f'/product/{self.product_image.pk}/update/',
# #                 {'product': self.product.pk, 'image': image},
# #                 content_type='multipart/form-data'
# #             )
# #         self.assertEqual(response.status_code, 200)




url = 'http://127.0.0.1:8000/product/image/31/update/'
files = {'image': open('PS C:\Users\HP\OneDrive\Images\.JPG', 'rb')}
data = {'product': '31'}
response = requests.put(url, files=files, data=data)

print(response.status_code)
print(response.json())