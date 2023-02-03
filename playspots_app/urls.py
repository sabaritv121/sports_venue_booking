from django.urls import path, include
from rest_framework import routers

from playspots_app import views
from playspots_app.views import BookingSlotViewSet

#Booking url
router = routers.DefaultRouter()
router.register('slots', BookingSlotViewSet,basename="slots")

urlpatterns = [
    path("",views.home,name='home'),

    path('api/',include(router.urls)),

    path('rank/<int:venue_id>/', views.rank),

]