from django.contrib import admin
from .models import Student


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'instagram', 'facebook')


admin.site.register(Student, StudentAdmin)
