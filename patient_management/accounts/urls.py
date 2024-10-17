from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('receptionist-dashboard/', views.receptionist_dashboard, name='receptionist_dashboard'),
]
