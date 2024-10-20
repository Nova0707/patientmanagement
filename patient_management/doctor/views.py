from django.shortcuts import render

# Create your views here.
def SetTimeSlotPage(request):
    return render(request,'doctor/set_time_slot.html')