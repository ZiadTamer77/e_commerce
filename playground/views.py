from django.shortcuts import render
from rest_framework.views import APIView
import requests
import logging

logger = logging.getLogger(__name__)


class HelloView(APIView):
    def get(request, self):
        try:
            logger.info("calling httpbin")
            requests.get("https://httpbin.org/delay/2")
            logger.info("Recieved the response")
        except requests.ConnectionError:
            logger.critical("httpbin is offline")
        return render(request, "hello.html", {"name": "zeyad"})
