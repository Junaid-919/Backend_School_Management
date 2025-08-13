from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Department, Designation, Subject

class CustomUserAdmin(UserAdmin):
    
    model = CustomUser
    list_display = ('username', 'full_name', 'role', 'department', 'designation', 'is_active_faculty')
    fieldsets = UserAdmin.fieldsets + (
        ("Role Information", {
            'fields': (
                'role', 'grade', 'full_name', 'phone_number', 'profile_photo',
                'employee_id', 'qualification', 'date_of_joining', 'subject_specialization',
                'department', 'designation', 'reporting_to', 'is_active_faculty',
                'tenure_start', 'tenure_end', 'achievements', 'office_contact',
                'access_level', 'system_notes', 'can_impersonate_users'
            )
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Subject)