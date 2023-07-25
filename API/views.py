from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
#from Travelcompanion.authentication import BasicAuthentication

class testView(APIView):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content={
                    "details": [
                        {
                        "user": "srikanth",
                        "city": "Hyderabad",
                        "state": "Telangana",
                        "country": "India",
                        "pincode": 500085,
                        "contact_details": [
                            {
                            "mobile": "9874563596",
                            "email": "srikanth@gmail.com"
                            }
                        ],
                        "age": 40,
                        "gender": "Male",
                        "organization": "Auxtomate"
                        }
                        ]}
        return Response(content)
