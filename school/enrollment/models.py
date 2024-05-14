from django.db import models
from student.models import Student


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Enrollment(BaseModel):
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
