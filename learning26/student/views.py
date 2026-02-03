from django.shortcuts import render

# Create your views here.

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
