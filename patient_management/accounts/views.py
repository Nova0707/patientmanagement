from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import User, Doctor, Receptionist, TimeSlot, Appointment

# Login views for doctors and receptionists
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'doctor':
                return redirect('doctor_dashboard')
            elif user.role == 'receptionist':
                return redirect('receptionist_dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

# Doctor's dashboard
@login_required
def doctor_dashboard(request):
    if request.user.role != 'doctor':
        return redirect('login')
    
    doctor = Doctor.objects.get(user=request.user)
    receptionists = Receptionist.objects.filter(doctor=doctor)
    slots = TimeSlot.objects.filter(doctor=doctor)
    
    context = {
        'doctor': doctor,
        'receptionists': receptionists,
        'slots': slots,
    }
    return render(request, 'accounts/doctor_dashboard.html', context)

# Receptionist's dashboard
@login_required
def receptionist_dashboard(request):
    if request.user.role != 'receptionist':
        return redirect('login')

    receptionist = Receptionist.objects.get(user=request.user)
    slots = TimeSlot.objects.filter(doctor=receptionist.doctor, is_booked=False)
    
    context = {
        'receptionist': receptionist,
        'slots': slots,
    }
    return render(request, 'accounts/receptionist_dashboard.html', context)

