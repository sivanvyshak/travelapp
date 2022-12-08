from django.http import HttpResponse
from django.shortcuts import render
from . models import place, people


# Create your views here.

def demo(request):
    obj = place.objects.all()
    obje = people.objects.all()
    return render(request, "index.html", {'result': obj, 'results': obje})

# def demop(request):
#
#     return render(request, "index.html", {'results': obje})
# def about(request):
#     return render(request, "about.html")

# def addition(request):
#     x = int(request.GET["num1"])
#     y = int(request.GET["num2"])
#     res = x+y
#     sub = x-y
#     mul = x*y
#     div = x / y

    # return render(request, 'result.html', {'addition' : res,'subtraction': sub, 'Multiplication':mul, 'Division':div})

