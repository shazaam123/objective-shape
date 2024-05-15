from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import StudentInformation, EducationBackground
from .serializers import StudentInformationSerializers, EducationBackgroundSerializers
from student.models import Student
from student.serializers import StudentSerializers, EducationBackgroundSerializers


@api_view(['GET', 'POST'])
def create_new_enrollment(request):
    if request.method == "POST":
        student_serializer = StudentInformationSerializers(data=request.data)
        education_serializer = EducationBackgroundSerializers(
            data=request.data)

        if student_serializer.is_valid() and education_serializer.is_valid():
            student_data = student_serializer.validated_data
            education_data = education_serializer.validated_data
            existing_student = Student.objects.filter(
                name=student_data["name"], name=education_data["high_school"]).first()
            if existing_student:
                existing_student_serializer = StudentSerializers(
                    existing_student)
                return Response(existing_student_serializer.data, status=200)
            else:
                student_serializer.save()
                education_serializer.save()
                return Response(student_serializer.data, status=201)
        else:
            return Response(student_serializer.error, status=400)
    else:
        student = Student.objects.all()
        serializer = StudentSerializers(student, many=True)
        return Response(serializer.data)
