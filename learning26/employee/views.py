from django.shortcuts import render,HttpResponse,redirect
from .models import Employee
from .forms import EmployeeForm,CourseForm

# Create your views here.
def employeeList(request):
  
    employees = Employee.objects.all().values()
   
    print(employees)
    return render(request, 'employee/employeeList.html',{"employees":employees})

def employeeFilter(request):
  
    employee = Employee.objects.filter(name ="raj").values()
   
    employee2 = Employee.objects.filter(post ="Developer").values()
    
    employee3 = Employee.objects.filter(name ="raja",post ="Developer").values()
  
   
    employee4 = Employee.objects.filter(age__gt=23).values()
    employee5 = Employee.objects.filter(age__gte=23).values()

   
    employee6 = Employee.objects.filter(post__exact="Developer").values()
    employee7 = Employee.objects.filter(post__iexact="developer").values()
   
    employee8 = Employee.objects.filter(name__contains="r").values()
    employee9 = Employee.objects.filter(name__icontains="R").values()

    
    employee10 = Employee.objects.filter(name__startswith="R").values()
    employee11 = Employee.objects.filter(name__endswith="R").values()
    employee12 = Employee.objects.filter(name__istartswith="R").values()
    employee13 = Employee.objects.filter(name__iendswith="R").values()

  
    employee14 = Employee.objects.filter(name__in=["raj","jay"]).values()    

   
    employee15 = Employee.objects.filter(age__range=[24,30]).values()    

 
    employee16 = Employee.objects.order_by("age").values()     
    employee17 = Employee.objects.order_by("-age").values()    

    employee18 = Employee.objects.order_by("-salary").values()  

    

  
    print("query 1",employee)
    print("query 2",employee2)
    print("query 3",employee3)
    print("query 4",employee4)
    print("query 5",employee5)
    print("query 6",employee6)   
    print("query 7",employee7) 
    print("query 8",employee8) 
    print("query 9",employee9) 
    print("query 10",employee10) 
    print("query 11",employee11) 
    print("query 12",employee12) 
    print("query 13",employee13) 
    print("query 14",employee14) 
    print("query 15",employee15) 
    print("query 16",employee16) 
    print("query 17",employee17) 
    return render(request, 'employee/employeeFilter.html')


def createEmployee(request):
    Employee.objects.create(name="ajay",age=23,salary=23000,post="HR",join_date="2022-01-01")
    return HttpResponse("EMPLOYEE IS CREATED")

def createEmployeeWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.save() 
        #return HttpResponse("EMPLOYEE CREATED...")
        return redirect("employeeList")
    else:
        
        form = EmployeeForm()         
        return render(request,"employee/createEmployeeForm.html",{"form":form})


def createCourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST) #csrftoken,form alll fileds data
        form.save() #create.. insert into table 
        return HttpResponse("COURSE CREATED...")
    else:
        form = CourseForm()
        return render(request,"employee/createCourse.html",{"form":form}) 
    

def deleteEmployee(request,id):

    print("id from url = ",id)
    Employee.objects.filter(id=id).delete(  )
    return redirect("employeeList")

def filterEmployee(request):
    print("filter employee called...")
    employees = Employee.objects.filter(age__gte=25).values()
    print("filter employees = ",employees)
    #return redirect("employeeList")
    return render(request,"employee/employeeList.html",{"employees":employees})


def sortemployees(request,id):
    if id==1:
          employee = Employee.objects.order_by("age").values()

    else:
        employee = Employee.objects.order_by("-age").values()
    
    return render(request,"employee/employeeList.html",{"employees":employee})


def updateEmployee(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        form.save()
        return redirect("employeeList")
    else:
        form = EmployeeForm(instance=employee)
        return render(request, "employee/updateEmployee.html", {"form": form})
