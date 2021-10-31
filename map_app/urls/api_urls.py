from django.urls import path
from django.urls.resolvers import URLPattern

from ..views.api_views import BookingRequest

app_name = "map_app"

urlpatterns = [
    path("booking_request/",BookingRequest.as_view(),name="BookingRequestAPIView")
]