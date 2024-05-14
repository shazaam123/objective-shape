from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers


@api_view(['GET', 'POST'])
def student_create(request):
    if request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            existing_student = Student.objects.filter(
                name=data['name']).first()
            if existing_student:
                existing_student_serializer = StudentSerializers(
                    existing_student)
                return Response(existing_student_serializer.data, status=200)
            else:
                serializer.save()
                return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    else:
        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        serializers = StudentSerializers(Student.objects.all(), many=True)
        return Response(serializers.data)
