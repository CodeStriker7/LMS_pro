from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # fieldsets - bu tahrirlash sahifasida ko'rinadigan bloklar
    fieldsets = UserAdmin.fieldsets + (
        ("LMS ma'lumotlari", {'fields': ('is_teacher', 'is_student', 'phone', 'bio', 'avatar')}),
    )
    
    # add_fieldsets - yangi user yaratayotganda ko'rinadigan maydonlar
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("LMS ma'lumotlari", {'fields': ('is_teacher', 'is_student', 'phone')}),
    )
    
    # list_display - foydalanuvchilar ro'yxatida ko'rinadigan ustunlar
    list_display = ['username', 'email', 'is_teacher', 'is_student', 'is_staff']

# Modelni yangi sozlamalar bilan ro'yxatdan o'tkazamiz
admin.site.register(User, CustomUserAdmin)