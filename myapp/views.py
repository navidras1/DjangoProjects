from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    a=5
    b=3
    return render(request,'index.html')