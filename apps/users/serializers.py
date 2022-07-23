from rest_framework import serializers

from .models import *

class FilterReviewSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data=data.filter(parent=None)
        return super().to_representation(data)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'
        # read_only_fields=('user',)

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Developer
        fields='__all__'
        # read_only_fields=('user',)



   


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



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','first_name','last_name','image','group','password','reviews_to_user']
    
    # developer=DeveloperSerializer(many=True,read_only=True)
    # customer=CustomerSerializer(many=True,read_only=True)
    reviews_to_user=ReviewSerializer(many=True,read_only=True)

    def create(self, validated_data):
        user = super().create(validated_data)
        password = validated_data['password']
        user.set_password(password)
        user.save()
        return user

# class ProfileSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=Profile
#         fields=['profile','profile__username','profile__first_name','profile__last_name','profile__image','profile__group']
#         # read_only_fields=('profile',)