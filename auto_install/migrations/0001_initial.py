# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-17 08:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='appgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appgroup', models.CharField(max_length=50)),
                ('appname', models.CharField(max_length=50)),
                ('warpath', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='apphost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostaddr', models.CharField(max_length=30)),
                ('username', models.CharField(default='root', max_length=20)),
                ('path', models.CharField(max_length=200)),
                ('appgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_install.appgroup')),
            ],
        ),
        migrations.CreateModel(
            name='auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_install.appgroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]