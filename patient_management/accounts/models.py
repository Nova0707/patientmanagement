from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Custom user model to handle different user roles
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('receptionist', 'Receptionist'),
    ]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='accounts_user_groups',  # Avoids clash with auth.User.groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='accounts_user_permissions',  # Avoids clash with auth.User.user_permissions
        blank=True
    )

# Doctor model to manage doctor-specific details
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    average_time = models.DurationField()
    min_time = models.DurationField()
    max_time = models.DurationField()

    def __str__(self):
        return self.user.username

# Receptionist model, linked to Doctor
class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# Patient model to store patient details
class Patient(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    check_in_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

# TimeSlot model to store available slots and their status
class TimeSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)
    booked_by = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

# Appointment model to manage bookings
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment for {self.patient.name} with {self.doctor.user.username}"
