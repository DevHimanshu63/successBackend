from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from Subapp.models import Admission,Team
from Subapp.models import Campus
from Subapp.models import Course,Testimonials
from Subapp.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    allcourse=Course.objects.all()
    allstudent=Campus.objects.all()
    # print(allcourse)
    context={'allpost':allcourse,'student':allstudent}
    return render(request,"./index.html",context)
    

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
        messages.error(request,"Message has not been send !")
        # messages.success(request,"your information has been sent successfully!")
    return redirect('/')


def admission(request):
    if request.method=="POST":
        name=request.POST['name']
        allCourse=request.POST['allCourse']
        email=request.POST['email']
        phone=request.POST['phone']
        query=request.POST['query']
        if len(name)<2:
            messages.error(request,"Enter your valid Name.")
        else:
            obj=Admission(fullName=name,stu_course=allCourse,Email=email,Phone=phone,query=query)
            obj.save()
            messages.success(request,"We will contact ASAP")
            return redirect('/admission')
    
    
    return render(request,"admission.html")

def team(request):
    Member=Team.objects.all
    Testimonial=Testimonials.objects.all
    context={'allmember':Member,'alltestimonial':Testimonial}
    return render(request,'team.html',context)