from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import AddProduct, ModifyProduct, DeleteProduct, ListProducts, RetrieveProduct, UploadProductImage, DeleteProductImage

urlpatterns = [
    path('product/list/', ListProducts.as_view(), name='list-products'),
    path('product/<int:pk>/', RetrieveProduct.as_view(), name='retrieve-product'),
    path('product/add/', AddProduct.as_view(), name='add-product'),
    path('product/<int:pk>/update/', ModifyProduct.as_view(), name='modify-product'),
    path('product/<int:pk>/delete/', DeleteProduct.as_view(), name='delete-product'),
    path('product/image/upload/<int:pk>/', UploadProductImage.as_view(), name='upload-product-image'),
    path('product/image/delete/<int:pk>/', DeleteProductImage.as_view(), name='delete-product-image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
