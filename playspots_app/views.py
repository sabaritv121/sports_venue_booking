from datetime import date, timedelta

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from playspots_app import serializers
from playspots_app.models import Booking
from playspots_app.serializers import BookingSerializer


def home(request):
    return HttpResponse('hi')


# class BookingCreateView(generics.CreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#
#
#     def perform_create(self, serializer_class):
#         # u = Booking.objects.filter('user')
#         # print(u)
#         print("hii")
#         slot = serializer_class.save(user = user)
#         print(slot)
#         print(slot.date)
#         print(slot.time_slot)
#
#         # check if the slot already exists for the same date and time
#         existing_slot = Booking.objects.filter(date=slot.date, time_slot=slot.time_slot,)
#         if existing_slot:
#             # raise serializers.ValidationError({'error': 'This slot is already booked'})
#             print("error")
#         else:
#             print("true")





class BookingSlotViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            slot_date = serializer.validated_data['date']
            slot_time = serializer.validated_data['time_slot']

            # Booking can only be done for the current month

            today = date.today()
            next_month = today + timedelta(days=30)
            if slot_date < today or slot_date > next_month:
                return Response("Booking can only be done for the current month.")

            # one slot can be booked by only once per day.

            elif Booking.objects.filter(date=slot_date,time_slot=slot_time).exists():
                return Response({"error": "User already booked  Slot  for the given date."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)