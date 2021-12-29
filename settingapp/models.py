from django.db import models
from django.utils.safestring import mark_safe

DEVICE_CHOICES = (
    ('All', 'All'),
    ('iOS', 'iOS'),
    ('Android', 'Android')
)


class BaseModel(models.Model):
    status = models.BooleanField(default=True, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class CompanySetting(BaseModel):
    company_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Company Name')
    contact_person = models.CharField(max_length=50, blank=False, null=False, verbose_name='Contact Person')
    address = models.CharField(max_length=255, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state_province = models.CharField(max_length=50, blank=False, null=False, verbose_name='State/Province')
    postal_code = models.CharField(max_length=15, blank=False, null=False, verbose_name='Postal Code')
    email = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False, verbose_name='Phone Number')
    mobile_number = models.CharField(max_length=20, blank=False, null=False, verbose_name='Mobile Number')
    fax = models.CharField(max_length=20, blank=False, null=False)
    website_url = models.CharField(max_length=150, blank=False, null=False, verbose_name='Website URL')

    class Meta:
        verbose_name_plural = 'CompanySettings'

    def __str__(self):
        return f'{self.company_name}'


class Localization(BaseModel):
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name='Default Country')
    date_format = models.CharField(max_length=50, blank=True, null=True, verbose_name='Date Format')
    timezone = models.CharField(max_length=50, blank=True, null=True, verbose_name='Timezone')
    language = models.CharField(max_length=50, blank=True, null=True, verbose_name='Default Language')
    currency_code = models.CharField(max_length=50, blank=True, null=True, verbose_name='Currency Code')
    currency_symbol = models.CharField(max_length=50, blank=True, null=True, verbose_name='Currency Symbol')

    class Meta:
        verbose_name_plural = 'Localizations'

    def __str__(self):
        return f'{self.country}'


class ThemeSetting(BaseModel):
    website_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Website Name')
    light_logo = models.ImageField(upload_to='settingapp/theme/', verbose_name='Light Logo', help_text='Recommended image size is 40px x 40px (Allowed size is 1MB)')
    favicon = models.ImageField(upload_to='settingapp/theme/', help_text='Recommended image size is 16px x 16px (Allowed size is 1MB)')

    class Meta:
        verbose_name_plural = 'ThemeSettings'

    def __str__(self):
        return f'{self.website_name}'

    def logo(self):
        if self.light_logo:
            return mark_safe('<img src="%s" style="width: auto; height: auto;"/>' % self.light_logo.url)
        else:
            return '__'
    logo.short_description = 'Logo'

    def get_favicon(self):
        if self.favicon:
            return mark_safe('<img src="%s" style="width: auto; height: auto;"/>' % self.favicon.url)
        else:
            return '__'
    get_favicon.short_description = 'Favicon'


class InvoiceSetting(BaseModel):
    invoice_prefix = models.CharField(max_length=50, blank=True, null=True, verbose_name='Invoice Prefix')
    invoice_logo = models.ImageField(upload_to='settingapp/invoice/', verbose_name='Invoice Logo', height_field='Recommended image size is 200px x 40px (Allowed size is 50MB)')

    class Meta:
        verbose_name_plural = 'InvoiceSettings'

    def __str__(self):
        return f'{self.invoice_prefix}'

    def logo(self):
        if self.invoice_logo:
            return mark_safe('<img src="%s" style="width: auto; height: auto;"/>' % self.invoice_logo.url)
        else:
            return '__'
    logo.short_description = 'Logo'


class Slider(BaseModel):
    title = models.CharField(max_length=100, blank=False, null=False)
    caption = models.CharField(max_length=250, default='', blank=False, null=False)
    photo_url = models.ImageField(upload_to='settingapp/sliders/%Y-%m-%d/', verbose_name='Photo URL', help_text='Allowed size is 500MB', blank=False, null=False)

    def get_caption(self):
        return self.caption[:30]

    def __str__(self):
        return self.title

    def banner_slider(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height:55px;" />' % self.photo_url.url)
        else:
            return '__'
    banner_slider.short_description = 'Banner'


class Notification(BaseModel):
    title = models.CharField(max_length=150)
    device = models.CharField(choices=DEVICE_CHOICES, max_length=10, default='All')
    photo_url = models.ImageField(upload_to='settingapp/notifications/%Y-%m-%d/', verbose_name='Photo URL', help_text='Allowed size is 500MB', blank=False, null=False)
    message = models.TextField()

    def __str__(self):
        return self.title

    def profile(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height:55px;" />' % self.photo_url.url)
        else:
            return '__'
    profile.short_description = 'Profile'

