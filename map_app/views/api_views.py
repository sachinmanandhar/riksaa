
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import RideRequestSerializer
class BookingRequest(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"data":"this is data"},status = 200)