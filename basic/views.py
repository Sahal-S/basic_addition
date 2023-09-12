from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def one(request):
    return render(request, 'one.html',{'name':'joseph'})
def two(request):
    n1=request.GET["num1"]
    n2=request.GET["num2"]
    res=int(n1)*int(n2)
    
    return HttpResponse(res)

