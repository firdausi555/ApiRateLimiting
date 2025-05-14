# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import SimpleRateThrottle
from rest_framework.throttling import ScopedRateThrottle
from .throttles import CustomViewThrottle
from rest_framework.permissions import AllowAny

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})
# api/views.py (continue)


class CustomThrottledView(APIView):
    throttle_classes = [CustomViewThrottle]
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "This is a custom throttled endpoint."})


class RootView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the API Rate Limiting Demo"})