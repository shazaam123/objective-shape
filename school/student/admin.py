from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']


admin.site.register(StudentInfo, StudentAdmin)
