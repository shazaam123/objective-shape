from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StudentInfo(BaseModel):
    student_id = models.ForeignKey(
        'enrollment.StudentInformation', on_delete=models.CASCADE, related_name='')
    education_id = models.ForeignKey(
        'enrollment.EducationBackground', on_delete=models.CASCADE, related_name='')
