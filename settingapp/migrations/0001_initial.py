# Generated by Django 4.0 on 2021-12-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Name')),
                ('contact_person', models.CharField(max_length=50, verbose_name='Contact Person')),
                ('address', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state_province', models.CharField(max_length=50, verbose_name='State/Province')),
                ('postal_code', models.CharField(max_length=15, verbose_name='Postal Code')),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('mobile_number', models.CharField(max_length=20, verbose_name='Mobile Number')),
                ('fax', models.CharField(max_length=20)),
                ('website_url', models.CharField(max_length=150, verbose_name='Website URL')),
            ],
            options={
                'verbose_name_plural': 'CompanySettings',
            },
        ),
        migrations.CreateModel(
            name='InvoiceSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('invoice_prefix', models.CharField(blank=True, max_length=50, null=True, verbose_name='Invoice Prefix')),
                ('invoice_logo', models.ImageField(height_field='Recommended image size is 200px x 40px (Allowed size is 50MB)', upload_to='settingapp/invoice/', verbose_name='Invoice Logo')),
            ],
            options={
                'verbose_name_plural': 'InvoiceSettings',
            },
        ),
        migrations.CreateModel(
            name='Localization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Default Country')),
                ('date_format', models.CharField(blank=True, max_length=50, null=True, verbose_name='Date Format')),
                ('timezone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Timezone')),
                ('language', models.CharField(blank=True, max_length=50, null=True, verbose_name='Default Language')),
                ('currency_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Currency Code')),
                ('currency_symbol', models.CharField(blank=True, max_length=50, null=True, verbose_name='Currency Symbol')),
            ],
            options={
                'verbose_name_plural': 'Localizations',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('device', models.CharField(choices=[('All', 'All'), ('iOS', 'iOS'), ('Android', 'Android')], default='All', max_length=10)),
                ('photo_url', models.ImageField(help_text='Allowed size is 500MB', upload_to='settingapp/notifications/%Y-%m-%d/', verbose_name='Photo URL')),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('caption', models.CharField(default='', max_length=250)),
                ('photo_url', models.ImageField(help_text='Allowed size is 500MB', upload_to='settingapp/sliders/%Y-%m-%d/', verbose_name='Photo URL')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThemeSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('website_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Website Name')),
                ('light_logo', models.ImageField(help_text='Recommended image size is 40px x 40px (Allowed size is 1MB)', upload_to='settingapp/theme/', verbose_name='Light Logo')),
                ('favicon', models.ImageField(help_text='Recommended image size is 16px x 16px (Allowed size is 1MB)', upload_to='settingapp/theme/')),
            ],
            options={
                'verbose_name_plural': 'ThemeSettings',
            },
        ),
    ]
