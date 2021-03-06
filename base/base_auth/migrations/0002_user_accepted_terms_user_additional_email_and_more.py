# Generated by Django 4.0.3 on 2022-03-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accepted_terms',
            field=models.BooleanField(default=False, verbose_name='accepted terms'),
        ),
        migrations.AddField(
            model_name='user',
            name='additional_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='additional email address'),
        ),
        migrations.AddField(
            model_name='user',
            name='email_token',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='email token'),
        ),
        migrations.AddField(
            model_name='user',
            name='read_new_terms',
            field=models.BooleanField(default=False, verbose_name='new terms read'),
        ),
        migrations.AddField(
            model_name='user',
            name='verified_email',
            field=models.BooleanField(default=True),
        ),
    ]
