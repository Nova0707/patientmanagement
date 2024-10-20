from django.urls import path
#imports related to page render
from doctor.views import (
    SetTimeSlotPage,
    )
from doctor.views_bl import (
    SetTimeSlotLogic,
)
urlpatterns = [
    # urls related to page rendering
    path('',SetTimeSlotPage,name="SetTimeSlotPage"),

    #urls related ti business logic
    path('set_time_slot/',SetTimeSlotLogic.as_view(),name="SetTimeSlotLogic"),
]