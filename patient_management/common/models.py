from django.db import models

# Create your models here.
#model related to user roles
class RoleMaster(models.Model):
    role = models.CharField(max_length=30,null=True,blank=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.role

#model related to access control
class ModuleMaster(models.Model):
    module_name = models.CharField(max_length=30,null=True,blank=True)
    keycode = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.module_name

class AccessControl(models.Model):
    module = models.ForeignKey(ModuleMaster,on_delete=models.CASCADE,related_name="module_access_control")
    is_view = models.BooleanField(default=False)
    is_add = models.BooleanField(default=False)
    is_edit = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)