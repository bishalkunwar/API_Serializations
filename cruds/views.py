from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import student
from .serializers import studentSerializer


# Create your views here.
@csrf_exempt
def students_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.ByteIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            student_data = student.objects.get(id=id)
            serializer = studentSerializer(student_data)
            return JsonResponse(serializer.data)

        student_data = student.objects.all()
        serializer = studentSerializer(student_data, many = True)
        return JsonResponse(serializer.data) 


    if request.methos == 'POST':
        json_data = request.body
        stream = io.ByteIO(json_data)
        student_data = JSONParser().parse(stream)
        serializer = studentSerializer(data=student_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    if request.method == 'PUT':
        json_data = request.body
        stream = io.ByteIO(json_data)
        student_data = JSONParser().parse(stream)
        id = student_data.get('id')
        stud = student.objects.get(id=id)
        serializer = studentSerializer(stu, data=student_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.ByteIO(json_data)
        student_data = JSONParser().parse(stream)
        id = student_data.get('id')
        stud = student.objects.get(id=id)
        stud.delete()

        return HttpResponse()