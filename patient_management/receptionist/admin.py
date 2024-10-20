from django.contrib import admin
from receptionist.models import (
    SlotTimeMorning, SlotTimeEvening
)
# Register your models here.
@admin.register(SlotTimeMorning)
class SlotTimeMorningAdmin(admin.ModelAdmin):
    list_display = ['id','start_time','end_time','number_of_slots','created_by','is_deleted']

@admin.register(SlotTimeEvening)
class SlotTimeEveningAdmin(admin.ModelAdmin):
    list_display = ['id','start_time','end_time','number_of_slots','created_by','is_deleted']