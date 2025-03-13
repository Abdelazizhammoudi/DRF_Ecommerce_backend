from django.urls import path
from .views import UpdateProductImage, ListProducts, RetrieveProduct, AddProduct, ModifyProduct, DeleteProduct, DeleteProductImage

urlpatterns = [
    path('product/', ListProducts.as_view(), name='list-products'),
    path('product/<int:pk>/', RetrieveProduct.as_view(), name='retrieve-product'),
    path('product/add/', AddProduct.as_view(), name='add-product'),
    path('product/<int:pk>/update/', ModifyProduct.as_view(), name='update-product'),
    path('product/<int:pk>/delete/', DeleteProduct.as_view(), name='delete-product'),
    path('product/image/<int:pk>/update/', UpdateProductImage.as_view(), name='update-product-image'),
    path('product/image/<int:pk>/delete/', DeleteProductImage.as_view(), name='delete-product-image'),
]