# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livedevice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MBEDCloudAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(default='https://api.us-east-1.mbedcloud.com')),
                ('api_key', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebHookAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=200, unique=True)),
                ('mbed_cloud_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livedevice.MBEDCloudAccount')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='webhook_auth',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='livedevice.WebHookAuth'),
            preserve_default=False,
        ),
    ]