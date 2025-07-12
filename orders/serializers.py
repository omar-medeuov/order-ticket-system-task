from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Ticket, Order

User = get_user_model()

class OrderSerializer(serializers.ModelSerializer):


    class Meta:
        model = Order
        fields = ("order_id", "user", "phone_number", "status", "comment")


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ("ticket_code", "item_code", "order", "status")


class TicketUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("status",)
