from django.urls import path
from . import views




urlpatterns= [
      path("home/",views.studentHome),
      path("dashboard/",views.studentDashboard),
      path("attendance/",views.studentAttendance),
      path("fees/",views.studentFees),
      path("login/",views.studentLogin),
      path("serviceList/",views.serviceList,name="serviceList"),
      path("createService/",views.createService,name="createService"),
      path('service/delete/<int:id>/', views.deleteService, name='deleteService'),



]
