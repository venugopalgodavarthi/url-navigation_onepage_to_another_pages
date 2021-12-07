from django.shortcuts import render

# Create your views here.

def demoa(request):
    return render(request,'sampleA.html')

def demob(request):
    return render(request,'sampleB.html')

