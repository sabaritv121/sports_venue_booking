from datetime import date, timedelta

from rest_framework import serializers

from playspots_app.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    date = serializers.DateField()

    def validate_slot_date(self, value):
        today = date.today()
        next_month = today + timedelta(days=30)
        if value < today or value > next_month:
            raise serializers.ValidationError("Booking can only be done for the current month.")
        return value
    class Meta:
        model = Booking
        fields = '__all__'

