from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Student(BaseModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdata = models.DateField()
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    citizenship = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.IntegerField()
    country = models.CharField(max_length=255)
    emergency_contact = models.CharField(max_length=255)
    emergency_first_name = models.CharField(max_length=255)
    emergency_last_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    language_list = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    graduation_date = models.DateField()
    school_address = models.CharField(max_length=255)
    school_city = models.CharField(max_length=255)
    school_state = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
