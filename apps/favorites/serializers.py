from rest_framework import serializers

from apps.favorites.models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id','to_user','user',)
        read_only_fields = ( 'user',)
        
    # def to_representation(self, instance):
    #     rep = super(FavoriteSerializer, self).to_representation(instance)
    #     rep['to_user'] = instance.user.username
    #     rep['user'] = instance.user.username
    #     return rep
