# Generated by Django 2.2.13 on 2020-06-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0013_auto_20200617_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcompany',
            name='address',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
