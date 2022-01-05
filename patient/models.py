from datetime import date
from django.db import models
from django.utils.safestring import mark_safe

from hospital.models import Doctor


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

MARITAL_CHOICES = (
    ('SI', 'Single'),
    ('MA', 'Married'),
    ('WI', 'Windowed'),
    ('SE', 'Separated'),
    ('NT', 'Not Specified')
)


class BaseModel(models.Model):
    status = models.BooleanField(default=True, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class BloodBank(BaseModel):
    blood = models.CharField(max_length=4)
    bag = models.CharField(max_length=5)

    def blood_group(self):
        return self.blood

    def __str__(self):
        return f'{self.blood} | {self.bag} bags'

    def bag_group(self):
        if self.bag == '0' or self.bag == '1':
            return f'{self.bag} bag'
        else:
            return f'{self.bag} bags'


class Patient(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patients')
    blood = models.ForeignKey(BloodBank, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(max_length=120)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=2)
    dob = models.DateField(verbose_name='Date of Birth')
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=120, blank=True, null=True)
    address = models.CharField(max_length=250)
    marital_status = models.CharField(choices=MARITAL_CHOICES, max_length=2, verbose_name='Marital Status')
    photo_url = models.ImageField(upload_to='patients/%Y-%m-%d/', verbose_name='Photo URL',
                                  help_text='Allowed size is 200MB', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def display_doctor(self):
        return f'{self.doctor.name}'

    def display_blood(self):
        return f'{self.blood.blood}'

    def get_patient_age(self):
        # age = datetime.date.today() - self.dob
        # return int((age).day/365.25)
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age

    def profile(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height: 30px;"/>' % self.photo_url.url)
        else:
            return '__'
    profile.short_description = 'Profile'

