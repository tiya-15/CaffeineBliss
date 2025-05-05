# coffee/api.py
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product_id', 'product_name', 'price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'name', 'email', 'phone', 'address', 
                 'payment_method', 'notes', 'total_amount', 
                 'created_at', 'items']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Custom action for additional functionality
    @action(detail=True, methods=['get', 'delete'])
    def manage_order(self, request, pk=None):
        """
        Custom endpoint to get or delete specific order
        """
        order = self.get_object()
        
        if request.method == 'GET':
            serializer = self.get_serializer(order)
            return Response(serializer.data)
            
        elif request.method == 'DELETE':
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)