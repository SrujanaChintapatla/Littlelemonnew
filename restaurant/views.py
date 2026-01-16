from django.shortcuts import render
from requests import Response
from .serializers import BookingSerializer
from .models import Booking
from django.http import HttpResponse

# Create your views here.
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