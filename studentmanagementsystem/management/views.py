from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from management.models import CustomUser

from management.forms import sandtform


# Create your views here.
def home(request):
    return render(request,'Home.html')

def teachersignup(request):
    return render(request,'teacher.html')
def studentsignup(request):
    return render(request,'student.html')
def principlesignup(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p = request.POST['p']
        c = request.POST['c']
        e = request.POST['e']
        f= request.POST['f']
        l = request.POST['l']
        a = request.POST['a']
        n= request.POST['n']
        if (p==c):
            r=CustomUser.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l,place=a,phone=n)
            r.is_principle=True
            r.save()
            return home(request)
        else:
            return HttpResponse('passwords are not same')
    return render(request,'principle.html')
@login_required
def studentsignup(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        c = request.POST['c']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        a = request.POST['a']
        n = request.POST['n']
        if (p == c):
            r = CustomUser.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l, place=a,
                                               phone=n)
            r.is_student=True
            r.save()
            return home(request)

        else:
            return HttpResponse("Passwords are not same")

    return render(request,'student.html')
@login_required
def teachersignup(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        c = request.POST['c']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        a = request.POST['a']
        n = request.POST['n']
        if (p == c):
            r = CustomUser.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l, place=a,
                                               phone=n)
            r.is_teacher=True
            r.save()
            return home(request)

        else:
            return HttpResponse("Passwords are not same")

    return render(request,'teacher.html')
def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        l = authenticate(username=u, password=p)
        if l and l.is_principle==True:
            login(request, l)
            return principlehome(request)
        elif l and l.is_student==True:
            login(request, l)
            return studenthome(request)
        elif l and l.is_teacher==True:
            login(request, l)
            return teacherhome(request)
        else:
            return HttpResponse("Invalid credentials")
    return render(request,'login.html')
def principlehome(request):
    return render(request,'principlehome.html')
def studenthome(request):
    return render(request,'studenthome.html')
def teacherhome(request):
    return render(request,'teacherhome.html')
def user_logout(request):
    logout(request)
    return user_login(request)
@login_required
def studentsview(request):
    students=CustomUser.objects.filter(is_student=True)
    return render(request,'studentsview.html',{'s':students})
@login_required
def teachersview(request):
    teachers=CustomUser.objects.filter(is_teacher=True)
    return render(request,'teachersview.html',{'t':teachers})
@login_required
def studentdetail(request,p):
    student=CustomUser.objects.get(id=p,is_student=True)
    return render(request,'studentdetail.html',{'g':student})
@login_required
def teacherdetail(request,p):
    teacher=CustomUser.objects.get(id=p,is_teacher=True)
    return render(request,'teacherdetail.html',{'e':teacher})
@login_required

def studentupdate(request,p):
    u=CustomUser.objects.get(id=p)
    if(request.method=="POST"):
        form=sandtform(request.POST,instance=u)
        if form.is_valid():
            form.save()
        return studentsview(request)
    form = sandtform(instance=u)
    return render(request, 'update.html', {'form': form})
@login_required
def teacherupdate(request,p):
    u=CustomUser.objects.get(id=p)
    if(request.method=="POST"):
        form=sandtform(request.POST,instance=u)
        if form.is_valid():
            form.save()
        return teachersview(request)
    form = sandtform(instance=u)
    return render(request, 'update.html', {'form': form})
@login_required
def studentdelete(request,p):
    d=CustomUser.objects.get(id=p)
    d.delete()
    return studentsview(request)
@login_required
def teacherdelete(request,p):
    d=CustomUser.objects.get(id=p)
    d.delete()
    return teachersview(request)





