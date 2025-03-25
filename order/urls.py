from django.urls import path
from .views import OrderCreateView, OrderListView, OrderDeleteView , OrderUpdateView, OrderStatusUpdateView

urlpatterns = [
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/update/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
    path('orders/list/', OrderListView.as_view(), name='order-list'),
    path('orders/status/<int:pk>/', OrderStatusUpdateView.as_view(), name='order-status-update'),
]