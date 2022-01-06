from django.db import models
from hospital.models import Doctor
from django.utils import timezone
from patient.models import Patient

SHIFT_CHOICES = (
    ('M', "Morning"),
    ('A', 'Afternoon'),
    ('E', "Evening")
)

STATUS_CHOICES = (
    ('PD', 'Pending'),
    ('CF', 'Confirmed'),
    ('CC', 'Cancelled')
)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Appointment(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField(default=timezone.now)
    shift = models.CharField(choices=SHIFT_CHOICES, max_length=15)
    time = models.TimeField(default=timezone.now)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default='Pending')
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.patient.name}-{self.doctor.name}'

    def patient_profile(self):
        return f'{self.patient.photo_url}'

    def get_first_letter(self):
        return f'{self.patient.name[:1]}'

    def patient_address(self):
        return f'{self.patient.address[:10]}'
