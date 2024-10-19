from django.shortcuts import render

# render pages
def BookAppointmentPage(request):
    return render(request,'receptionists/BookingPage.html')