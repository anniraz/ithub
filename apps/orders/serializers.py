from rest_framework import serializers

from apps.orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =Order
        fields = ('id','to_user','user',)
        read_only_fields = ("id", 'user',)


class Order1Serializer(serializers.ModelSerializer):
    class Meta:
        model =Order
        fields = ('id','to_user','user',)
