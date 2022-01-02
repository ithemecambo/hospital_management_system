from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.safestring import mark_safe

USER_SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class AccountManager(BaseUserManager):
    def create_user(self, email, password, is_active=False, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('User must have an email address')
        if not password:
            raise ValueError('User must have an password')
        user = self.model(email=self.normalize_email(email))
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self, email, password):
        user = self.create_user(email, password=password, )
        user.staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        return self.create_user(email, password, is_active=True, is_staff=True, is_admin=True)


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=30, null=True, verbose_name='Last Name')
    sex = models.CharField(choices=USER_SEX_CHOICES, default='Male', max_length=10, verbose_name='Sex')
    email = models.EmailField(unique=True, null=False, verbose_name='Email')
    password = models.CharField(max_length=128, verbose_name='Password')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    fax = models.CharField(max_length=20, blank=True, null=True, verbose_name='Fax')
    photo_url = models.ImageField(upload_to='avatars/%Y-%m-%d/', blank=True, null=True, verbose_name='Photo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    get_full_name.short_description = 'Full Name'

    def profile(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: 25px; height: 25px;"/>' % self.photo_url.url)
        else:
            return '__'

    profile.short_description = 'Profile'

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_phone(self):
        if self.phone == '':
            return ''
        return f'{self.phone}'

    def get_fax(self):
        if self.fax == '':
            return ''
        return f'{self.fax}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


