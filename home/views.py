from django.shortcuts import render, redirect
from .models import *

# Create your views here.


 
def student(request):
    return render(request,"home/home.html")
    
def adminsite(request):
    if Student.objects.all():
        student_dtl=Student.objects.all()
        student_cnt=Student.objects.all().count()
        student_cnt_a=Student.objects.filter(status="active").count()
        student_cnt_a=Student.objects.filter(status="active").count()
        student_cnt_i=student_cnt - student_cnt_a

        data={
            'student_dtl':student_dtl,
            'student_cnt':student_cnt,
            'student_cnt_a':student_cnt_a,
            'student_cnt_i':student_cnt_i,
            
        }
    
    
    return render(request,"home/adminsite.html",data)

# register student
def studentRegister(request):
    if request.method == "POST":
        name=request.POST["name"]
        contact=request.POST["contact"]
        email=request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"]
        rule="student"
        status="active"
        newStudent=Student(name=name,contact=contact,email=email,username=username,password=password,rule=rule,status=status)
        print(newStudent)
        newStudent.save()
        

        return redirect("/home/adminsite")
    else:
        return render(request,"home/addstudent.html")

# active student
def activeStudent(request):
    student_dtl=Student.objects.filter(status="active")
    data={
            'student_dtl':student_dtl,
    }
    

    return render(request,"home/activestudent.html",data)

# inactive student
def inactiveStudent(request):
    student_dtl=Student.objects.filter(status="inactive")
    data={
            'student_dtl':student_dtl,
     }
    return render(request,"home/inactivestudent.html",data)

def studentStatus(request,id):
    student_dtl=Student.objects.get(id=id)
    if student_dtl.status == "active":
        student_dtl.status="inactive"
        student_dtl.save()
    else:
        student_dtl.status="active"
        student_dtl.save()
    return redirect("/home/adminsite")

def studentDetails(request):
    student_dtl=Student.objects.filter(id=1)

    data={
            'user':student_dtl,
            'student_dtl':student_dtl,
     }
    return render(request,"student/studentsite.html",data)
    

    