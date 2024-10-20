from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.models import CustomUserAccounts, UserRole
from django.core.mail import send_mail
from django.conf import settings
from django.views import View

class SignUpView(View):
    def get(self, request):
        return render(request, 'authentication/signup.html')

    def post(self, request):
        email = request.POST.get('email')
        verification_code = "1234"  
        send_mail(
            'Email Verification',
            f'Your verification code is {verification_code}',
            settings.EMAIL_HOST_USER,
            [email],
        )
        request.session['temp_email'] = email
        request.session['verification_code'] = verification_code
        return redirect('verify_email')

class VerifyEmailView(View):
    def get(self, request):
        return render(request, 'authentication/verify_email.html')

    def post(self, request):
        code = request.POST.get('code')
        if code == request.session.get('verification_code'):
            # Create and save user account
            CustomUserAccounts.objects.create(
                email=request.session.get('temp_email'),
                is_active=True
            )
            return redirect('login')
        else:
            # Handle invalid code
            return render(request, 'authentication/verify_email.html', {'error': 'Invalid code'})

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('/redirect_based_on_role/')
        return render(request, 'authentication/login.html', {'error': 'Invalid credentials'})

class RoleRedirectView(View):
    def get(self, request):
        user_role = UserRole.objects.get(user=request.user).role.role
        if user_role == 'Doctor':
            return redirect('/doctor/dashboard/')
        elif user_role == 'Receptionist':
            return redirect('/receptionist/booking_page/')
        return redirect('/login/')
