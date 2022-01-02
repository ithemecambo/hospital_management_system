from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

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

VEHICLE_CHOICES = (
    ('O', 'Owned'),
    ('C', 'Contractual')
)

WORK_PER_DAY_CHOICES = (
    ('MO', 'Monday'),
    ('TU', 'Tuesday'),
    ('WE', 'Wednesday'),
    ('TH', 'Thursday'),
    ('FR', 'Friday'),
    ('SA', 'Saturday'),
    ('SU', 'Sunday')
)

TERM_CHOICES = (
    ('FP', 'Full Time'),
    ('PT', 'Part Time')
)

LOCATION_CHOICES = (
    ('BLN', 'Banlung'),
    ('BMY', 'Banteay Meanchey'),
    ('BTB', 'Battambang'),
    ('BVT', 'Bavet'),
    ('KCM', 'Kampong Cham'),
    ('KCN', 'Kampong Chhnang'),
    ('KSU', 'Kampong Speu'),
    ('KTM', 'Kampong Thom'),
    ('KPT', 'Kampot'),
    ('KDL', 'Kandal'),
    ('KEP', 'Kep'),
    ('KKG', 'Koh Kong'),
    ('KIE', 'Kratie'),
    ('MKR', 'Mondulkiri'),
    ('OMY', 'Oddor Meanchey'),
    ('OSS', 'Overseas'),
    ('PLN', 'Pailin'),
    ('PPH', 'Phnom Penh'),
    ('PPT', 'Poipet'),
    ('PSK', 'Preah Sihanouk'),
    ('PVR', 'Preah Vihear'),
    ('PRN', 'Prey Veng'),
    ('PUT', 'Pursat'),
    ('RTR', 'Rattanakiri'),
    ('SRP', 'Siem Reap'),
    ('SAL', 'Sre Ambel'),
    ('STN', 'Stung Treng'),
    ('SRN', 'Svay Rieng'),
    ('TKO', 'Takeo'),
    ('THO', 'Takhmao'),
    ('TKM', 'Tboung Khmum')
)


class BaseModel(models.Model):
    status = models.BooleanField(default=True, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Department(BaseModel):
    title = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='departments/', help_text='Allowed size is 10MB', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Departments'

    def __str__(self):
        return f'{self.title}'

    def icon(self):
        if self.logo:
            return mark_safe('<img src="%s" style="width: 25px; height: 25px;"/>' % self.logo.url)
        else:
            return '__'

    icon.short_description = 'Icon'

    def get_description(self):
        return self.description[:50]


class Ambulance(BaseModel):
    vehicle_number = models.CharField(max_length=20, verbose_name='Vehicle Number')
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    year = models.IntegerField(default=1988)
    driver_name = models.CharField(max_length=50, verbose_name='Driver Name')
    driver_contact = models.CharField(max_length=20, verbose_name='Driver Contact')
    vehicle_type = models.CharField(choices=VEHICLE_CHOICES, max_length=2, default='Owned', verbose_name='Vehicle Type')
    driver_license = models.BooleanField(default=True, verbose_name='Driver License')
    photo_url = models.ImageField(upload_to='ambulances/', verbose_name='Photo URL', help_text='Allowed size is 200MB',
                                  blank=True, null=True)

    def __str__(self):
        return f'{self.driver_name} {self.vehicle_number}'

    def vehicle(self):
        return f'{self.make} {self.model} {self.year}'

    def photo(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: 65px; height: auto;"/>' % self.photo_url.url)
        else:
            return '__'

    photo.short_description = 'Photo'


class Doctor(BaseModel):
    name = models.CharField(max_length=120)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=2, default='Male')
    dob = models.DateField(verbose_name='Date of Birth')
    nationality = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=120, blank=True, null=True)
    address = models.CharField(max_length=250)
    speciality = models.ManyToManyField(to='Speciality', related_name='doctors')
    language = models.ManyToManyField(to='Language', related_name='doctors')
    department = models.ManyToManyField(to='Department', related_name='doctors')
    photo_url = models.ImageField(upload_to="doctors/%Y-%m-%d/", verbose_name='Photo URL',
                                  help_text='Allowed size is 200MB')
    twitter = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def speciality_name(self):
        return f'{self.specaility.name}'

    def language_name(self):
        return f'{self.language.name}'

    def department_title(self):
        return f'{self.department.title}'

    def profile(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height: 30px;"/>' % self.photo_url.url)
        else:
            return '__'

    profile.short_description = 'Profile'


class Article(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=120)
    tag = models.ManyToManyField(to='Speciality', related_name='articles')
    thumbnail = models.ImageField(upload_to='articles/')
    cover_url = models.ImageField(upload_to='articles/%Y-%m-%d/', verbose_name='Cover URL',
                                  help_text='Allowed size is 200MB')
    image1 = models.ImageField(upload_to='articles/%Y-%m-%d/', verbose_name='Image 1',
                               help_text='Allowed size is 500MB', blank=True, null=True)
    image2 = models.ImageField(upload_to='articles/%Y-%m-%d/', verbose_name='Image 2',
                               help_text='Allowed size is 500MB', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}-{self.doctor.name}'


class Speciality(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Specialities'

    def __str__(self):
        return f'{self.name}'


class Language(BaseModel):
    name = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    code = models.CharField(max_length=5)
    dial_code = models.CharField(max_length=5)
    flag = models.ImageField(upload_to='languages/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def get_flag(self):
        if self.flag == '':
            return ''
        return f'{self.flag}'

    def get_dial_code(self):
        if self.dial_code == '':
            return ''
        return f'+{self.dial_code}'

    get_dial_code.short_description = 'Dial Code'

    def logo(self):
        if self.flag:
            return mark_safe('<img src="%s" style="width: 25px; height: auto;"/>' % self.flag.url)
        else:
            return '__'
    logo.short_description = 'Logo'


class Experience(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='experiences')
    company_name = models.CharField(max_length=100, verbose_name='Company Name')
    location = models.CharField(max_length=250)
    logo_url = models.ImageField(upload_to='experiences/%Y-%m-%d/', verbose_name='Logo URL',
                                 help_text='Allowed size is 100MB', blank=True, null=True)
    position = models.CharField(max_length=100)
    start_work = models.DateField(verbose_name='Start Work')
    end_work = models.DateField(verbose_name='End Work')
    responsibilities = models.CharField(max_length=250)
    skill_used = models.CharField(max_length=250, verbose_name='Skill Used')
    description = models.TextField()

    def __str__(self):
        return f'{self.doctor}'

    def logo(self):
        if self.logo_url:
            return mark_safe('<img src="%s" style="width: 25px; height: 25px;"/>' % self.logo_url.url)
        else:
            return '__'

    logo.short_description = 'Logo'


class Education(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='educations')
    school_name = models.CharField(max_length=150, verbose_name='School Name')
    major = models.CharField(max_length=150)
    start_year = models.DateField(verbose_name='Start Year')
    end_year = models.DateField(verbose_name='End Year')
    logo_url = models.ImageField(upload_to='educations/%Y-%m-%d/', verbose_name='Logo URL',
                                 help_text='Allowed size is 100MB', blank=True, null=True)
    activities_societies = models.CharField(max_length=250, verbose_name='Activity Societies')
    description = models.TextField()

    def __str__(self):
        return f"{self.doctor}"

    def logo(self):
        if self.logo_url:
            return mark_safe('<img src="%s" style="width: 25px; height: 25px;"/>' % self.logo_url.url)
        else:
            return '__'

    logo.short_description = 'Logo'


class Schedule(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedules')
    available_days = models.CharField(choices=WORK_PER_DAY_CHOICES, max_length=3, default='Monday',
                                            verbose_name='Available Days')
    start_time = models.TimeField(default=timezone.now, verbose_name='Start Time')
    end_time = models.TimeField(default=timezone.now, verbose_name='End Time')
    description = models.TextField()

    def __str__(self):
        return f'{self.doctor.name}'
