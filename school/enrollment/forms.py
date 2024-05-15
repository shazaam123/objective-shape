from django import forms
from .model import StudentInformation, EducationBackground

class StudentInformationForm(forms.ModelForm):
    class Meta:
        model = StudentInformation
        fields = "__all__"

class EducationBackgroundForm(forms.ModelForm):
    class Meta:
        model = EducationBackground
        fields = "__all__"