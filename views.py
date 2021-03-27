from django.shortcuts import render
from .models import student
from .serializers import studentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

def student_details(request,pk):
    stu = student.objects.get(id=pk)
    serializer = studentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

