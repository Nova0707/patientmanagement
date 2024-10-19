from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.user_account_manager import UserAccountManager

#imports related to user roles
from common.models import RoleMaster
    
class CustomUserAccounts(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(null=True,blank=True)
    is_deleted = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
class UserRole(models.Model):
    user = models.ForeignKey('accounts.CustomUserAccounts', on_delete=models.CASCADE, related_name='user_role')
    role = models.ForeignKey(RoleMaster, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)