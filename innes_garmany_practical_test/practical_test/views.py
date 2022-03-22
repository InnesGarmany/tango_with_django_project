from django.shortcuts import render
from django.http import HttpResponse
from practical_test.models import GACourse

def index(request):
    courseList= GACourse.objects.order_by("startDate")
    
    contextDict = {}
    #for course in courseList:
    contextDict['courses'] = courseList

    return render(request, 'practical_test/index.html', context = contextDict)
