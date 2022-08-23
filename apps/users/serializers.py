from rest_framework import serializers

from .models import *

class FilterReviewSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data=data.filter(parent=None)
        return super().to_representation(data)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['user','from_choice']
        # read_only_fields=('user',)

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:

        model=Developer
        fields=['user','direction','level','about']
        # read_only_fields=('user',)



class DeveloperInfoSerializer(serializers.ModelSerializer):
    class Meta:

        model=Developer
        fields=('user','direction','level','about')




class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer=self.parent.parent.__class__(value,context=self.context)
        return serializer.data

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields=['id','text','rating','time_pub','children','to_user']
        read_only_fields=('auth',)

class ReviewSerializer(serializers.ModelSerializer):

    children=RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class=FilterReviewSerializer
        model=Reviews
        fields=['id','text','rating','time_pub','children']
        read_only_fields=('auth',)

class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields=['rating']





class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additional_info
        fields = ['id','user','first_name','last_name','image','phone','description']
        read_only_fields=('user',)


class AdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additional_info
        fields = ['id','user','first_name','last_name','image','phone','description']

class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','developer','customer','password','user_info','reviews_to_user']
    
    developer=DeveloperInfoSerializer(many=True,read_only=True)
    customer=CustomerSerializer(many=True,read_only=True)
    reviews_to_user=ReviewSerializer(many=True,read_only=True)
    user_info=AdditionalSerializer(many=True,read_only=True)

    def create(self, validated_data):
        user = super().create(validated_data)
        password = validated_data['password']
        user.set_password(password)
        user.save()
        return user





