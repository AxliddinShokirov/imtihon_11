from django.db import models
from django.utils import timezone

# Create your models here.
class User_names(models.Model):
    name=models.CharField(max_length=255)
    surname=models.CharField(max_length=255)
    age=models.IntegerField()
    email=models.EmailField(max_length=255)
    phone_number=models.CharField(max_length=20)
    image=models.ImageField()
    def __str__(self):

        return self.name
    

class Xodimlar_name(models.Model):
    name=models.CharField(max_length=255)
    surname=models.CharField(max_length=255)
    age=models.IntegerField()
    email=models.EmailField(max_length=255)
    phone_number=models.CharField(max_length=20)
    address=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class Attendance(models.Model):
    xodimlar_name=models.ForeignKey(Xodimlar_name, on_delete=models.CASCADE, related_name='attendance')
    date=models.DateField(default=timezone.now)
    isinstance=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.xodimlar_name.name} - {self.date}"
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['xodimlar_name', 'date'], name='unique_attendance_per_day')
        ]
      















