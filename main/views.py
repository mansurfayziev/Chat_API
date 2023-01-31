from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import User,Message
from .serializers import UserSerializer,MessageSerializer
from rest_framework import status
from rest_framework.response import Response

def HomeView(request):
    return render(request,'home.html')


def DocsView(request):
    return render(request,'docs.html')

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_params = ["id_message"]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filter_kwargs = dict()
        for param in self.filter_params:
            value = self.request.query_params.get(param)
            if value is not None:
                filter_kwargs[param] = value
        queryset = queryset.filter(**filter_kwargs)
        return queryset

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_params = ["id_user"]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filter_kwargs = dict()
        for param in self.filter_params:
            value = self.request.query_params.get(param)
            if value is not None:
                filter_kwargs[param] = value
        queryset = queryset.filter(**filter_kwargs)
        return queryset

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)