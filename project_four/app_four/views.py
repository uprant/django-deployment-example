from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"app_four/index.html")

def other(request):
    return render(request,"app_four/other.html")

def relative(request):
    return render(request,"app_four/relative.html")