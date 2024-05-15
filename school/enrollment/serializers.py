from rest_framework import serializers
from .models import StudentInformation, EducationBackground 

class StudentInformationSerializers(serializers.Serializer):
    class Meta:
        model = StudentInformation
        fields = "__all__"

class EducationBackgroundSerializers(serializers.Serializer):
    class Meta:
        model = EducationBackground
        fields = "__all__"