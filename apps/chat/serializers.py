from apps.users.models import User
from rest_framework import serializers
from apps.chat.models import Message



class MessageSerializer(serializers.ModelSerializer):
    # sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    # receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Message
        fields = ['id','sender', 'receiver', 'message', 'timestamp']
        read_only_fields=('sender',)

    # def to_representation(self, instance):
    #     rep = super(MessageSerializer, self).to_representation(instance)
    #     rep['sender'] = instance.user.username
    #     rep['receiver'] = instance.user.username
    #     return rep
    
        # read_only_fields=('sender',)


class ChatSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']