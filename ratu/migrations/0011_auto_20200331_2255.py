# Generated by Django 2.0.9 on 2020-03-31 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratu', '0010_auto_20200331_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='short_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='state',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
