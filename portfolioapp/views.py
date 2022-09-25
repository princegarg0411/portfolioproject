from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')

def first(request):
    return render(request,'first.html')

def about(request):
    return render(request,'about.html')

def work(request):
    return render(request,'work.html')

def contact(request):
    return render(request,'contact.html')

def project(request):
    return render(request,'project.html')

def project2(request):
    return render(request,'project2.html')