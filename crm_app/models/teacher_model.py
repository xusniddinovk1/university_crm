from .auth_user import *
from django.db import models


class Course(BaseModel):
    objects = None
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title


class Departments(BaseModel):
    objects = None
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title


class Teacher(BaseModel):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    departments = models.ManyToManyField(Departments, related_name="teachers")
    course = models.ManyToManyField(Course, related_name="teachers")
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.user.phone_number})"
