from rest_framework import serializers

from apps.orders.models import Order,MakeOrder

class OrderSerializer(serializers.ModelSerializer):
    # location = serializers.SerializerMethodField('get_alternate_name')
    class Meta:
        model =Order
        fields = ('id','to_user','user',)
        read_only_fields = ("id", 'user',)

    # def to_representation(self, instance):
    #     rep = super(OrderSerializer, self).to_representation(instance)
    #     rep['to_user'] = instance.user.username
    #     rep['user'] = instance.user.username
    #     return rep

    # def get_alternate_name(self, obj):
    #     return obj.alternate_name



class MakeOrderSerializer(serializers.ModelSerializer):
    # location = serializers.SerializerMethodField('get_alternate_name')
    class Meta:
        model =MakeOrder
        fields = '__all__'
        read_only_fields = ("id", 'user',)

