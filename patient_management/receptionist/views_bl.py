from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication

#response related imports
from utility.common_response import common_response
class BookAppointmentLogic(APIView):
    authentication_classes=[SessionAuthentication]
    def post(self,request):
        print(request.data)
        return common_response(status_code = 201, message="Booking created!")