# Generated by Django 4.1.3 on 2023-03-30 10:30

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('p_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=40)),
                ('p_color', models.CharField(default='', max_length=40)),
                ('p_price', models.IntegerField()),
                ('p_quantity', models.IntegerField()),
                ('p_dimensions', models.CharField(default='', max_length=255)),
                ('p_category', models.CharField(default='', max_length=255)),
                ('p_status', models.CharField(default='', max_length=255)),
                ('p_images', models.CharField(default='', max_length=255)),
            ],
            options={
                'db_table': 'ProductRecords',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('s_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=40)),
                ('s_email', models.CharField(default='', max_length=255)),
                ('s_address', models.CharField(default='', max_length=255)),
                ('s_staffmembers', models.IntegerField()),
                ('s_quality_ofWood', models.CharField(default='', max_length=255)),
                ('s_category_ofProduct', models.CharField(default='', max_length=255)),
                ('s_phoneNumber', models.BigIntegerField()),
                ('s_passwords', models.CharField(default='', max_length=10)),
            ],
            options={
                'db_table': 'SellerRecords',
            },
        ),
        migrations.CreateModel(
            name='threeDfiles',
            fields=[
                ('req_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Status', models.CharField(default='', max_length=255)),
                ('Image1', models.CharField(default='', max_length=255)),
                ('p_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='three_d_file', to='shop.products')),
                ('s_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='three_d_file', to='shop.seller')),
            ],
            options={
                'db_table': 'threeDfiles',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='s_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='shop.seller'),
        ),
        migrations.CreateModel(
            name='OrderRecords',
            fields=[
                ('o_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Product_name', models.CharField(default='', max_length=255)),
                ('Product_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('Buyers_name', models.CharField(default='', max_length=255)),
                ('BuyersAddress', models.CharField(default='', max_length=255)),
                ('BuyersContactNumber', models.BigIntegerField()),
                ('ShippingStatus', models.CharField(default='', max_length=255)),
                ('City_name', models.CharField(default='', max_length=255)),
                ('Country_name', models.CharField(default='', max_length=255)),
                ('p_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shop.products')),
                ('s_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shop.seller')),
            ],
            options={
                'db_table': 'OrderRecords',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_seller', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
