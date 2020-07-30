# Generated by Django 2.2 on 2020-07-30 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=75, verbose_name='Email address')),
                ('Contact', models.IntegerField(verbose_name='Contact Number')),
                ('Address', models.CharField(max_length=400)),
            ],
        ),
    ]