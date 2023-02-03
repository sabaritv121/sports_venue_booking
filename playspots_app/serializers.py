from datetime import date, timedelta

from rest_framework import serializers

from playspots_app.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    date = serializers.DateField()

    class Meta:
        model = Booking
        fields = ('id','venue','user','time_slot','date')


