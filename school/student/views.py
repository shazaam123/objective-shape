from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers


@api_view(["GET", "POST"])
def student_create(request):
    if request.method == "POST":
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            existing_student = Student.objects.filter(name=data["name"]).first()
            if existing_student:
                existing_student_serializer = StudentSerializers(existing_student)
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


@api_view(["GET"])
def student_list(request):
    if request.method == "GET":
        serializers = StudentSerializers(Student.objects.all(), many=True)
        return Response(serializers.data)
    else:
        return Response()


@api_view(["GET", "PUT"])
def student_update(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = StudentSerializers(student)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = StudentSerializers(student)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_BAD_REQUEST)
