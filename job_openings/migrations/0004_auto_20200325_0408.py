# Generated by Django 3.0.4 on 2020-03-25 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_openings', '0003_auto_20200311_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]