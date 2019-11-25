from django.contrib import admin

# Register your models here.
from .models import UserProfile,UserInfo

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone')
    list_filter = ('phone',)

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'school')
    list_filter = ('school',)