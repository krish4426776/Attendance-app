from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User  
from django.contrib.auth.views import LoginView 
from .models import Room , Attendance , Notification
from . forms import UserEditForm , AttendanceForm , Roomform , NotiicationForm
from datetime import date

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required 
from django.db.models import Q


from django.http import HttpResponse


# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


def RegisterPage(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    context = {'form':form}
    return render(request,'base/register.html',context)

@login_required(login_url=  'login')
def EditProfile(request , pk):
    user = User.objects.get(id=pk)
    form = UserEditForm(instance=user)
    if not request.user.groups.filter(name='Admin').exists():
        return HttpResponse("YOU ARE NOT ALLOWED HERE", status=403) 
    if request.method == 'POST':
        form = UserEditForm(request.POST,instance=user)
        if form.is_valid():
           
            form.save()
            return redirect ( 'home' )

    context = {'form' : form}
    return render (request , 'base/edit.html' , context)


def CreateAttendanceRoom(request):
    form = Roomform()
    if not request.user.groups.filter(name='Admin').exists():
        return HttpResponse("YOU ARE NOT ALLOWED HERE", status=403) 
    if request.method=='POST':
        form = Roomform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form':form}
    return render (request , 'base/createroom.html' , context)










def CreateAttendance(request):
    if Attendance.objects.filter(user=request.user, date=date.today()).exists():
        return HttpResponse("You have already done the attendance for today.")


    form = AttendanceForm()
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            att= form.save(commit=False)
            att.user = request.user
            att.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request,'base/attend.html' , context )


def AttendanceList(request):
    q = request.GET.get('q', '')

    attendance = Attendance.objects.filter (

        Q(date__icontains=q) |
        Q(user__username__icontains=q) 
        
    )
        


    
    if not request.user.groups.filter(name='Admin').exists():
        return HttpResponse("YOU ARE NOT ALLOWED HERE", status=403) 
    context = {'attendance' : attendance}
    return render(request,'base/attendancelist.html' , context)

def home(request):
    user = User.objects.all()
    
    room = Room.objects.all()
    notification = Notification.objects.all()
    context = {'users':user , 'room':room  , 'notifications':notification}
    
    return render (request , 'base/home.html' , context)

def index(request , pk):
    room=Room.objects.get(id=pk)
    context = {'room':room}
    return render(request , 'base/index.html' , context)



def UserView(request):
    user = User.objects.all()
    if not request.user.groups.filter(name='Admin').exists():
        return HttpResponse("YOU ARE NOT ALLOWED HERE", status=403) 
    context = {'user':user}
    return render (request , 'base/users.html' , context)


def Deleteuser(request , pk):
    user = User.objects.get(id=pk)
    
    if request.method=='POST':
        user.delete()
        
        return redirect('home')
    context={'obj':user}
    return render(request,'base/delete.html',context)

def Deleteroom(request , pk):
    room = Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    context={'obj':room}
    return render(request,'base/delete.html',context)


def ViewAttendance(request):
    user = request.user
    info = user.attendance_set.all()
    context={'info':info}
    return render(request , 'base/viewatt.html' , context)

def CreateNotification(request):
    form = NotiicationForm()
    if request.method=='POST':
        form=NotiicationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context={'form':form}
    return render(request,'base/notification.html', context)

def DeleteNotification(request , pk):
    notification = Notification.objects.get(id=pk)
    if request.method=='POST':
        notification.delete()
        return redirect('home')
    context={'obj':notification}
    return render(request,'base/delete.html',context)




