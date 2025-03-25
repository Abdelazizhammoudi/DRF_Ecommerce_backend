
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('order/', include('order.urls')),
    path('admin/login/', views.obtain_auth_token),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]

if settings.DEBUG:
    # Serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


