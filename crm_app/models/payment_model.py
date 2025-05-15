from django.db import models
from .student_model import Student


class Payment(models.Model):
    objects = None
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Pending', 'Pending')],
                              default='Pending')

    def __str__(self):
        return f"{self.student.user.phone_number} - {self.amount} - {self.status}"
