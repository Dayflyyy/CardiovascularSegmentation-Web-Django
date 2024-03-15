from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.


# 加入医生表
from .models import *


class DoctorAdmin(UserAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'sex', 'age', 'department', 'phone', 'introduction', 'photo')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_superuser', 'is_staff'),
            'description': _('Designates whether this user should be treated as '
                             'active, and whether they have all permissions.')
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'name', 'sex', 'age', 'department', 'phone', 'introduction',
                'photo'),
        }),
    )
    list_display = ('email', 'name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(Doctor, DoctorAdmin)



class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('id',)

class NIfTIImageAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'dimensions', 'voxel_size', 'data_type')
    list_filter = ('patient',)
    search_fields = ('patient',)
    ordering = ('id',)

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'content')
    list_filter = ('patient',)
    search_fields = ('patient',)
    ordering = ('id',)


