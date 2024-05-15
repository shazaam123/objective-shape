from django.contrib import admin
from .models import EducationBackground, StudentInformation
# Register your models here.
class EducationInline(admin.StackedInline):
    model = EducationBackground
    extra = 0

class StudentAdmin(admin.ModelAdmin):
    inlines = [EducationInline]

admin.site.register(StudentInformation, StudentInformation)