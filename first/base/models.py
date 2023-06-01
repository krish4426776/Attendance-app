from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Attendance(models.Model):
    choices = (
        ('present' , 'PRESENT'),
        ('abscent' , 'ABSCENT'),

    )
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    date = models.DateField(default=timezone.now, editable=False) 
    status = models.CharField(max_length=10 , choices=choices , default='abscent')

    def __str__(self):
      return f"{self.user.username} - {self.date}"
    class Meta:
        ordering = ['-date']



    
class Room(models.Model):
   name = models.CharField(max_length=200)
   created = models.DateTimeField(auto_now_add=True)
   datee = models.DateField(null=True)

   def __str__(self):
        return f"{self.name} - {self.datee}"
   
class Notification(models.Model):
    description = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    class Meta:
        ordering = ['-created']



 
