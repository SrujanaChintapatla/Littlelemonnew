from django.shortcuts import render
from requests import Response
from .serializers import BookingSerializer,MenuSerializer
from .models import Booking,Menu
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import viewsets, generics

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def BookingView(request):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return HttpResponse(serializer.data, content_type='application/json')

    if request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return HttpResponse(serializer.errors,content_type='application/json')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
@api_view(['GET','POST'])
def register(request):
    User.objects.create_user(
        username=request.data['username'],
        password=request.data['password']
    )
    return Response({'message': 'User created'})