from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView 
from .views import CustomLoginView 

urlpatterns = [
    path('' , views.home , name='home'),
    path('login/', CustomLoginView.as_view() , name='login' ),
    path('logout/', LogoutView.as_view(next_page='login'),name= 'logout'),
    path('room/<str:pk>/',views.index , name='index'),
    path('register/',views.RegisterPage , name='register'),
    path('edit/<str:pk>/',views.EditProfile , name='edit'),
    path('attendance',views.CreateAttendance , name='attend' ),
    path('attendanceroom',views.CreateAttendanceRoom , name='createatt'),
    path('attendancelist' , views.AttendanceList , name='list'),
    path('edituser' , views.UserView , name='useredit'),
    path('deleteuser/<str:pk>/' , views.Deleteuser , name='delete'),
    path('deleteroom/<str:pk>/' , views.Deleteroom , name='deleteroom'),
    path('viewattendance/' , views.ViewAttendance , name='view'),
    path('notification/' , views.CreateNotification , name='notify'),
    path('deletenotification/<str:pk>/' , views.DeleteNotification , name='deletenoti'),
    
    

]