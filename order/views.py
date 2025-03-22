from rest_framework import generics, permissions, status
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response

# Create Order (Public)
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to create orders

    def perform_create(self, serializer):
        # Set status to 'pending' by default
        serializer.save(status='pending')

# List Orders (Admin only)
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.select_related('product').all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'status': 'success',
            'count': queryset.count(),
            'data': serializer.data
        })

# Delete Order (Admin only)
class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can delete orders

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                'status': 'success',
                'message': f'Order #{instance.id} deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Order not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def get_success_headers(self, data):
        headers = super().get_success_headers(data)
        headers['X-Admin-Action'] = 'order-deleted'
        return headers


#update for the status of the order solde or not 
class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]
    http_method_names = ['patch']

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, 
            data=request.data, 
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)