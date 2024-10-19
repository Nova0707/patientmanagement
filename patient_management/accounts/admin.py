from django.contrib import admin
from accounts.models import (
    CustomUserAccounts,UserRole
)
# Register your models here.
@admin.register(CustomUserAccounts)
class CustomUserAccountsAdmin(admin.ModelAdmin):
    list_display=['id','email','is_superuser','is_active','created_on','created_by']

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['id','user','role','is_deleted']
