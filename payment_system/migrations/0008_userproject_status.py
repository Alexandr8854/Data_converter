# Generated by Django 3.0.7 on 2020-11-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0007_auto_20201109_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproject',
            name='status',
            field=models.CharField(blank=True, choices=[('invited', 'Invited'), ('active', 'Active'), ('removed', 'Removed')], default='invited', max_length=7),
        ),
    ]
