from django.shortcuts import render
from django.http import HttpResponse

# #testing templates
me = {"you" :"person","self" :"papa"}
def temp(self):
    return HttpResponse("<h1>My name is {} {} </h1>".format(me["you"],me["self"]))

# #testing views
wow = {'call':"My response is how're you doing"}
def index(request):
    return HttpResponse("<h1><b>It Worked</b></h1>")
    
def home(request):
    return render(request, "home.html", wow)