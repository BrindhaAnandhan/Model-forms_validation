from django.shortcuts import render
from app.models import *
from app.forms import *
#from django.http import HttpResponse

# Create your views here.
def Studentview(request):
    ESO = StudentForm()
    data = {'ESO': ESO, 'valid': ' '}
    if request.method == "POST":
        DESO = StudentForm(request.POST)
        if DESO.is_valid():
            DESO.save()
            return render(request, "display.html", data)
        else:
            data["valid"] = "***Invalid data***"
            return render(request, "display.html", data)
    
    return render(request, "display.html", data)