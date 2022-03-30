# Generated by Django 4.0.3 on 2022-03-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Email Address')),
                ('name', models.CharField(max_length=255)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff Status')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active Status')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]