# Generated by Django 4.1.3 on 2023-04-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_pricingtool'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='p_threedkinks',
            field=models.CharField(default='null', max_length=2000),
        ),
    ]
