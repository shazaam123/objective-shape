from django.db import models
from enrollment.models import StudentInformation, EducationBackground


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Student(BaseModel):
    student_id = models.ForeignKey(
        StudentInformation, on_delete=models.CASCADE, related_name='')
    education_id = models.ForeignKey(
        EducationBackground, on_delete=models.CASCADE, related_name='')
