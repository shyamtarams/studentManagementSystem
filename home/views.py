from django.shortcuts import render, redirect
from .models import *
from home.forms import studentRegisterForm

from accounts.models import myUser

from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.


# def signup(request):
#     if request.method == 'POST':
#         form = studentRegisterForm(request.POST)
#         print(form)
#         if form.is_valid():
#             rule = form.cleaned_data.get('rule')
#             status = form.cleaned_data.get('status')
#             print(rule)
#             print(status)

#             form.save()

#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=raw_password)
#             print(user)
#             login(request, user)
#             return redirect('/home/adminsite')
#     else:
#         form = studentRegisterForm()
#     return render(request, 'home/addstudent.html', {'form': form})

def login(request):
    if request.method=='POST':
        try:
            un=request.POST['username']
            pw=request.POST['password']
            # if Login.objects.get(username=un,password=pw):
                
            user=Login.objects.get(username=un,password=pw)
            request.session['log_id']=user.id 
            return redirect('/home/studentDetails/')
        except Exception as err:
            return redirect("/home/login")
    else:
        return render(request,"home/home.html")


 
def student(request):
    return render(request,"home/home.html")

@login_required(login_url='/accounts/login/')
def adminsite(request):
    data={}
    if Student.objects.filter(rule="student"):
        student_dtl=Student.objects.filter(rule="student")
        student_cnt=Student.objects.filter(rule="student").count()
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

        login=Login(username=username,password=password)
        login.save()

        newStudent=Student(name=name,contact=contact,email=email,username=username,password=password,rule=rule,status=status,login=login)
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
    try:
        id= request.session['log_id']
        user=Login.objects.get(id=id)
        student_dtl=Student.objects.filter(id=1)

        data={
                'user':user,
                'student_dtl':student_dtl,
        }
        return render(request,"student/studentsite.html",data)
    except:
        return redirect("/home/login/")
    

def logout(request):
    try:
        del request.session['log_id']
        return redirect("/home/login/")
    except:
        return redirect("/home/login/")
    

def updateStudent(request):
    try:
        id= request.session['log_id']
        user=Login.objects.get(id=id)
        if Student.objects.get(login=user.id,status="active"):
            student_dtl=Student.objects.get(login=user.id,status="active")
            if request.method=="POST":
                name=request.POST["name"]
                contact=request.POST["contact"]
                email=request.POST["email"]
                username=request.POST["username"]
                password=request.POST["password"]
                rule="student"
                status="active"

                update_data=Student.objects.get(login=user.id)
                update_data.name=name
                update_data.contact=contact
                update_data.email=email
                update_data.username=username
                update_data.password=password
                update_data.rule=rule
                update_data.status=status
                update_data.save()
                
                return redirect("/home/updatedetails/")
            else:
                data={
                    'user':user,
                    'student_dtl':student_dtl,
                }
                return render(request,"student/studentupdate.html",data)
        elif Student.objects.get(login=user.id,status="inactive"):
            return redirect("/home/studentDetails/")
    except:
        return redirect("/home/studentDetails/")

   



