from django.contrib import admin
from common.models import (
    RoleMaster,ModuleMaster,AccessControl
)
# Register your models here.
@admin.register(RoleMaster)
class RoleMasterAdmin(admin.ModelAdmin):
    list_display = ['id','role','is_deleted']

@admin.register(ModuleMaster)
class ModuleMasterAdmin(admin.ModelAdmin):
    list_display = ['id','module_name','keycode','is_deleted']

@admin.register(AccessControl)
class AccessControlAdmin(admin.ModelAdmin):
    list_display = ['id','module','is_view','is_add','is_edit','is_delete','is_deleted']