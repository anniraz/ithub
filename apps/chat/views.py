from apps.users.models import User 
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response


from apps.chat.models import *
from apps.chat.serializers import MessageSerializer

class ChatApiView(generics.ListCreateAPIView):
    serializer_class=MessageSerializer
    # queryset=Message

    # def perform_create(self, serializer):
    #     return serializer.save(sender=self.request.user)

    def get_queryset(self):
        user=self.request.user
        return Message.objects.filter(sender=user)
        
class ChatDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=MessageSerializer

    def perform_create(self, serializer):
        return serializer.save(sender=self.request.user)

    def get(self, request, *args, **kwargs):
        sender = self.request.user
        chat_list=Message.objects.filter(sender=sender)
        chat_serial=MessageSerializer(chat_list).data
        return Response(chat_serial)
        

class ChatToMeApiView(generics.ListAPIView):
    serializer_class=MessageSerializer


    def get_queryset(self):
        user=self.request.user
        return Message.objects.filter(receiver=user)




# lass UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         user = User.objects.get(id=pk)
#         user_serial = UserSerializer(user).data
#         reviews = Reviews.objects.filter(auth_id = pk)
#         lst = []
#         for i in reviews:
#             lst.append(i.rating)

#         rating_sum = sum(lst)
#         if len(lst)<=0:
#             rating_sum = 'нет отзывов'
#         else:
#             rating_sum = round(rating_sum / len(lst), 1)

#         user_serial['Reviews'] = rating_sum

#         return Response(user_serial)













# from django.http.response import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from apps.chat.models import Message                                                   # Our Message model
# from apps.chat.serializers import MessageSerializer, UserSerializer # Our Serializer Classes
# # Users View
# @csrf_exempt                                                              # Decorator to make the view csrf excempt.
# def user_list(request, pk=None):
#     """
#     List all required messages, or create a new message.
#     """
#     if request.method == 'GET':
#         if pk:                                                                      # If PrimaryKey (id) of the user is specified in the url
#             users = User.objects.filter(id=pk)              # Select only that particular user
#         else:
#             users = User.objects.all()                             # Else get all user list
#         serializer = UserSerializer(users, many=True, context={'request': request}) 
#         return JsonResponse(serializer.data, safe=False)               # Return serialized data
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)           # On POST, parse the request object to obtain the data in json
#         serializer = UserSerializer(data=data)        # Seraialize the data
#         if serializer.is_valid():
#             serializer.save()                                            # Save it if valid
#             return JsonResponse(serializer.data, status=201)     # Return back the data on success
#         return JsonResponse(serializer.errors, status=400)   

# @csrf_exempt
# def message_list(request, sender=None, receiver=None):
#     """
#     List all required messages, or create a new message.
#     """
#     if request.method == 'GET':
#         messages = Message.objects.filter(sender_id=sender, receiver_id=receiver)
#         serializer = MessageSerializer(messages, many=True, context={'request': request})
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MessageSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)