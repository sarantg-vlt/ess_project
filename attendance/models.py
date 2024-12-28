from datetime import datetime, timedelta
from django.db import models
from authentication.models import Employee, Manager, Shift, Location, Supervisor


# Create your models here.
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    notes = models.TextField()
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    in_status = models.CharField(max_length=20, null=True, blank=True)
    out_status = models.CharField(max_length=20, null=True, blank=True)
    overtime = models.CharField(max_length=20, null=True, blank=True)
    total_working_hours = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    timezone = models.CharField(max_length=100, null=True, blank=True)
    isp = models.CharField(max_length=100, null=True, blank=True)
    total_present_days = models.FloatField(default=0.0)


class ResetRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, blank=True)  # Removed 'name=True'
    date = models.DateField()
    request_type = models.CharField(max_length=50)
    request_description = models.TextField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    

# In attendance/models.py
class PermissionHour(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    reason = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    duration = models.DurationField(default=timedelta(), blank=True)  # New field for total hours
    requested_at = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(Manager, null=True, blank=True, on_delete=models.SET_NULL)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    @property
    def total_hours(self):
        delta = datetime.combine(datetime.today(), self.end_time) - datetime.combine(datetime.today(), self.start_time)
        return delta.seconds // 3600

    def __str__(self):
        return f"{self.employee.employee_name} - {self.date} - {self.status}"
    
class AttendanceOverview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance_records")
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=50)  
    check_in = models.TimeField()
    check_out = models.TimeField()
    work_hours = models.DecimalField(max_digits=5, decimal_places=2)  


def _str_(self):
    return f"Attendance for {self.employee} on {self.date}"
class Meta:
    verbose_name = "Attendance Overview"
    verbose_name_plural = "Attendance Overviews"
    


class Schedule(models.Model):
    ROLE_CHOICES = [
        ('UI/UX Designer', 'UI/UX Designer'),
        ('React Developer', 'React Developer'),
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Tester', 'Tester'),
        ('DevOps', 'DevOps'),
    ]

    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    interviewer = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)
    participant = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.date} - {self.role} - {self.participant}"
    

class DepartmentActiveJob(models.Model):
    role = models.CharField(max_length=255)
    experience_level = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50)
    openings = models.IntegerField()

    def __str__(self):
        return f'{self.role} - {self.experience_level}'
    
class CalendarEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.title} - {self.date} ({self.start_time} to {self.end_time})"
    
class Offer(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.position}"
    

from django.utils.timezone import now
from datetime import datetime, timedelta, timezone
class Employee_attendance(models.Model):
    
    username = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
from datetime import time, datetime


class Shift_attendance(models.Model):
    employee = models.CharField(max_length=100)
    date = models.DateField()
    
    start_time = models.TimeField(null=True, blank=True)  # Ensure this cannot be null
    end_time = models.TimeField(null=True, blank=True)
    break_time = models.IntegerField()
    shift_number = models.IntegerField(unique=True) 
    

    def __str__(self):
        return f"{self.employee.name} - {self.date}"
    def __str__(self):
        return f"Shift from {self.start_time} to {self.end_time}"

    def duration(self):
       
        total_time = (datetime.combine(now().date(), self.end_time) - 
                      datetime.combine(now().date(), self.start_time))
        return total_time - self.break_time

class Holiday(models.Model):
    
    date = models.DateField(unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"Holiday on {self.date}: {self.description}"
    


