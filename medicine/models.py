from django.db import models
from django.utils.safestring import mark_safe


class BaseModel(models.Model):
    status = models.BooleanField(default=True, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Manufacturer(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    balance = models.FloatField(default=0.0)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Category(BaseModel):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='categories/', help_text='Allowed size is 10MB', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def logo(self):
        if self.icon:
            return mark_safe('<img src="%s" style="width: 25px; height: 25px;"/>' % self.icon.url)
        else:
            return '__'
    logo.short_description = 'Logo'


class MedicineType(BaseModel):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='medicinetypes/', help_text='Allowed size is 10MB', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def logo(self):
        if self.icon:
            return mark_safe('<img src="%s" style="width: 25px; height: 25px;"/>' % self.icon.url)
        else:
            return '__'
    logo.short_description = 'Logo'


class Unit(BaseModel):
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='units/', help_text='Allowed size is 20MB', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def logo(self):
        if self.icon:
            return mark_safe('<img src="%s" style="width: auto; height: 30px;"/>' % self.icon.url)
        else:
            return '__'
    logo.short_description = 'Logo'


class Medicine(BaseModel):
    barcode_or_qrcode = models.CharField(max_length=50, verbose_name='Barcode or QR Code')
    medicine_name = models.CharField(max_length=100, verbose_name='Medicine Name')
    strength = models.CharField(max_length=100, blank=True, null=True)
    generic_name = models.CharField(max_length=50, verbose_name='Generic Name')
    box_size = models.CharField(max_length=20, blank=True, null=True, verbose_name='Box Size')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='medicines')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='medicines')
    medicine_type = models.ForeignKey(MedicineType, on_delete=models.CASCADE, blank=True,
                                      null=True, related_name='medicines', verbose_name='Medicine Type')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True,
                             null=True, related_name='medicines')
    medicine_shelf = models.CharField(max_length=50, blank=True, null=True, verbose_name='Medicine Shelf')
    manufacturer_price = models.FloatField(default=0.0, verbose_name='Manufacturer Price')
    sell_price = models.FloatField(default=0.0, verbose_name='Sell Price')
    tax = models.FloatField(default=0.0)
    vat = models.FloatField(default=0.0)
    photo_url = models.ImageField(upload_to='medicines/%Y-%m-%d/', verbose_name='Photo URL',
                                  help_text='Allowed size is 200MB', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.medicine_name} {self.manufacturer}'

    def product_name(self):
        return f'{self.medicine_name} {self.manufacturer}'

    def stock_price(self):
        return f'${self.manufacturer_price}'

    def sell_out_price(self):
        return f'${self.sell_price}'

    def profile(self):
        if self.photo_url:
            return mark_safe('<img src="%s" style="width: auto; height: 30px;"/>' % self.photo_url.url)
        else:
            return '__'
    profile.short_description = 'Profile'

