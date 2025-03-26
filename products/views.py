from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404  # Import get_object_or_404
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer
import logging
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.middleware.csrf import CsrfViewMiddleware
# from .models import User
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

logger = logging.getLogger(__name__)

# Add Product View (handles multiple images)
class AddProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        product = serializer.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ProductImage.objects.create(product=product, image=image)

# Update Product View
class ModifyProduct(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
    parser_classes = (MultiPartParser, FormParser)

# Delete Product View
class DeleteProduct(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []

# List All Products View
class ListProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []

# Retrieve Single Product View
class RetrieveProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []

# Upload Product Image View
class UploadProductImage(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        serializer.save(product=product)

# Update Product Image View
class UpdateProductImage(generics.UpdateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = []
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            logger.error(f"Serializer errors: {serializer.errors}")
            logger.error(f"Request data: {request.data}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Product Image View
class DeleteProductImage(generics.DestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = []
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        image = self.get_object()
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({'message': 'Welcome to the admin dashboard!'})

class ValidateAdminView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]  # Add IsAdminUser

    def get(self, request):
        try:
            user_data = {
                'username': request.user.username,
                'password': request.user.password,
                'isAdmin': True  # Explicitly set since IsAdminUser ensures this
            }
            return Response(user_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': 'Validation failed'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@method_decorator(csrf_exempt, name='dispatch')
class AdminLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        if not user.is_staff:
            logger.warning(f"Unauthorized login attempt by user: {user.username}")
            return Response({'error': 'Access denied: Not an admin'}, status=403)

        token, created = Token.objects.get_or_create(user=user)
        logger.info(f"Admin user {user.username} logged in successfully.")
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

# class CustomLoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
        
#         if user:
#             return Response({'success': True}, status=200)
#         return Response({'error': 'Invalid credentials'}, status=400)

        
# class CustomLoginView(APIView):
#     permission_classes = [AllowAny]
#     authentication_classes = []  # Disable authentication for this view

#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, *args, **kwargs):
#         return Response({'detail': 'Login GET method not supported. Please use the POST method to login.'})

#     def dispatch(self, request, *args, **kwargs):
#         # Disable CSRF protection for this view
#         setattr(request, '_dont_enforce_csrf_checks', True)
#         return super().dispatch(request, *args, **kwargs)