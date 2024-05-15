from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Student(BaseModel):
    
    school_name = models.CharField(max_length=255)
    graduation_date = models.DateField()
    school_address = models.CharField(max_length=255)
    school_city = models.CharField(max_length=255)
    school_state = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
