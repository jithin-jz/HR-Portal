from django.contrib import admin
from .models import UserProfile



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'place', 'salary')
    search_fields = ('user__username', 'position', 'place', 'salary')
    list_filter = ('position', 'place')


admin.site.register(UserProfile, UserProfileAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'check_in_time', 'check_out_time')  # Fields to display in the list view
    list_filter = ('user', 'check_in_time', 'check_out_time')  # Optional: filters for the list view
    search_fields = ('user__username',)  # Search by username


