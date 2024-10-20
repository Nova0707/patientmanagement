from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from utility.common_response import common_response
from doctor.models import (
    SlotTimeMorning, SlotTimeEvening
    )
#response related imports
from utility.common_response import common_response
class SetTimeSlotLogic(APIView):
    authentication_classes=[SessionAuthentication]
    def post(self,request):
        '''
        created by must be a user of type doctor
        '''
        currently_loggedin_user = request.user
        print(request.data)
        {'start_time_morning': '09:00', 'end_time_morning': '12:00', 'number_of_slots_morning': '18', 'start_time_evening': '13:00', 'end_time_evening': '18:00', 'number_of_slots_evening': '30'}
        # morning shift
        start_time_morning = request.data.get('start_time_morning')
        end_time_morning = request.data.get('end_time_morning')
        number_of_slots_morning = request.data.get('number_of_slots_morning')

        previous_morning_slots_morning = SlotTimeMorning.objects.filter(created_by = currently_loggedin_user).first()
        if previous_morning_slots_morning:
            previous_morning_slots_morning.start_time = start_time_morning
            previous_morning_slots_morning.end_time = end_time_morning
            previous_morning_slots_morning.number_of_slots=number_of_slots_morning
            previous_morning_slots_morning.save()
        else:
            SlotTimeMorning.objects.create(
                start_time=start_time_morning,
                end_time=end_time_morning,
                number_of_slots=number_of_slots_morning,
                created_by=currently_loggedin_user,
            )
        
        
        #evening shift
        start_time_evening = request.data.get('start_time_evening')
        end_time_evening = request.data.get('end_time_evening')
        number_of_slots_evening = request.data.get('number_of_slots_evening')
        previous_morning_slots_evening = SlotTimeMorning.objects.filter(created_by = currently_loggedin_user).first()
        if previous_morning_slots_evening:
            previous_morning_slots_evening.start_time = start_time_evening
            previous_morning_slots_evening.end_time = end_time_evening
            previous_morning_slots_evening.number_of_slots=number_of_slots_evening
            previous_morning_slots_evening.save()
        else:
            SlotTimeEvening.objects.create(
                start_time=start_time_evening,
                end_time=end_time_evening,
                number_of_slots=number_of_slots_evening,
                created_by=currently_loggedin_user,
            )
        

        return common_response(status_code = 201, message="Booking created!")