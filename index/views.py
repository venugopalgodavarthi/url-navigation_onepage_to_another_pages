from django.shortcuts import render

# Create your views here.

def indexA(request,id):
    return render(request,'indexA.html',{'id':id})