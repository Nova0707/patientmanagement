from django.contrib import admin
from .models import User, Doctor, Receptionist, Patient, TimeSlot, Appointment

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Receptionist)
admin.site.register(Patient)
admin.site.register(TimeSlot)
admin.site.register(Appointment)
