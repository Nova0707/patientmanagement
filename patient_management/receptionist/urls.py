from django.urls import path
#imports related to page render
from receptionist.views import (
    BookAppointmentPage,
    )
from receptionist.views_bl import (
    BookAppointmentLogic,
)
urlpatterns = [
    # urls related to page rendering
    path('',BookAppointmentPage,name="BookAppointmentPage"),

    #urls related ti business logic
    path('book_appointment/',BookAppointmentLogic.as_view(),name="BookAppointmentLogic"),
]