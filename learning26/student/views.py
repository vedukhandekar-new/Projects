from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from .models import Service
from .forms import ServiceForm




def studentHome(request):
    return render(request,"student/studentHome.html")

def studentDashboard(request):
    student = {"name":"Ved","age":"21","city":"Ahmedabad","Course":"Python"}
    return render(request,"student/studentDashboard.html",student)

def studentAttendance(request):
    return render(request,"student/studentAttendance.html")


def studentFees(request):
    return render(request,"student/studentFees.html")

def studentLogin(request):
    return render(request, "student/studentLogin.html")


def serviceList(request):
    services = Service.objects.all()
    return render(request,"student/serviceList.html",{"services":services})

def deleteService(request, id):
    if request.method == "POST":
        service = get_object_or_404(Service, pk=id)

        service_name = service.serviceName  # use correct field name

        service.delete()

        messages.success(
            request,
            f'"{service_name}" service is deleted successfully.'
        )

    return redirect('serviceList')


def createService(request):

    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
        else:
            return render(request,"student/createService.html",{"form":form})    
    else:
        form = ServiceForm()
        return render(request,"student/createService.html",{"form":form})