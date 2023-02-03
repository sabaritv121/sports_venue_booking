import calendar
from datetime import date, timedelta


from django.db.models import Sum, Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from playspots_app.models import Booking
from playspots_app.serializers import BookingSerializer

# Create your views here.
def home(request):
    return HttpResponse('WELCOME')





class BookingSlotViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            slot_date = serializer.validated_data['date']
            slot_time = serializer.validated_data['time_slot']
            venue_id =  serializer.validated_data['venue']

            # Booking can only be done for the current month

            today= date.today()
            year = today.year
            month = today.month
            last_day = calendar.monthrange(year, month)[1]
            end_date=date(year, month, last_day)
            if slot_date < today or slot_date> end_date:
                return Response("Booking can only be done for the current month.")

            # slot can be booked only once per day.

            elif Booking.objects.filter(date=slot_date,time_slot=slot_time,venue = venue_id).exists():
                return Response({"error": "The Slot is already booked."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#Categorize venues based on booking count

def rank(request,venue_id):
    today = date.today()
    month = today.month

    bookings=Booking.objects.filter(date__month=month,venue=venue_id)
    booking_count=len(bookings)
    if booking_count>15:
        data = {'result': 'GOLD'}
    elif booking_count>10 and booking_count<15:
        data = {'result': 'SILVER'}
    elif booking_count<10 and booking_count>1:
        data = {'result': 'BRONZE'}
    return JsonResponse({'data':data ,'booking_count':booking_count})








