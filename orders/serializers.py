from rest_framework import serializers

from .models import Ticket, Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("order_id", "username", "phone_number", "status", "comment")