from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from Subapp.models import Campus
from Subapp.models import Course
from Subapp.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    allcourse=Course.objects.all()
    allstudent=Campus.objects.all()
    # print(allcourse)
    context={'allpost':allcourse,'student':allstudent}
    return render(request,"index.html",context)
    

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        content=request.POST['content']
        if len(name)<2  or len(content)<5:
            messages.error(request,"Enter your valid Name or Message !")
        else:
            obj=Contact(name=name,email=email,content=content)
            obj.save()
            messages.success(request,"Message has been send !")
            return redirect('/')
        
    else:
        # return HttpResponse("message has not been send")
        messages.error(request,"Message ha not been send !")
        # messages.success(request,"your information has been sent successfully!")
    return redirect('/')


def admission(request):

    return render(request,"admission.html")
    