from django.http import HttpResponse
from django.shortcuts import render

def test(request):
         return HttpResponse("Hello")

def AboutUs(request):
        return render(request,"aboutus.html")


def ContactUs(request):
    return render(request,"contactus.html")

def home(request):
    return render(request,"home.html")  

def movies(request):
    return render(request,"movie.html")  
def show(request):
    return render(request,"show.html")  
def new(request):
    return render(request,"new.html")  

def recipe(request):
     ingredient = ["noodles","tomato","gravy"]
     information = {"name":"chinese","time":20,"ingredient":ingredient}
     return render(request,"recipe.html",information)

def team(request):
     players = ["rohit sharma(captain)","hardik pandya","suryakumar yadav","krishnan(wc)"]
     data = {"teamname":"Mumbai Indians","trophys":5,"players":players}
     return render(request,"team.html",data)
def school(request):
     activities = ["gaming","sports","drama"]
     data = {"schoolname":"St mary school","fees":20000,"activities":activities}
     return render(request,"school.html",data)