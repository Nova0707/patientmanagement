from django.db import models
from accounts.models import (
    CustomUserAccounts
    )
# Create your models here.
class Receptionists(models.Model):
    user = models.ForeignKey(CustomUserAccounts,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10,null=True,blank=True)

#time_duration = variable in view in minutes
class SlotTimeMorning(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    number_of_slots = models.IntegerField()
    created_by = models.ForeignKey(CustomUserAccounts,on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"Slot from {self.start_time} to {self.end_time}"
    
class SlotTimeEvening(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    number_of_slots = models.IntegerField()
    created_by = models.ForeignKey(CustomUserAccounts,on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"Slot from {self.start_time} to {self.end_time}"