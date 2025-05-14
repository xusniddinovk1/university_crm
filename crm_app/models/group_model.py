from .teacher_model import *


class Day(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title


class Rooms(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title


class GroupStudent(BaseModel):
    title = models.CharField(max_length=25, unique=True)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, related_name='groups')
    teacher = models.ManyToManyField(Teacher, related_name="groups_taught")
    start_date = models.DateField()
    end_date = models.DateField()
    descriptions = models.CharField(max_length=500, null=True, blank=True)
    students = models.ManyToManyField('User', related_name='group_students', blank=True,
                                      limit_choices_to={'is_student': True})

    def __str__(self):
        return self.title
