# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-07-30 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenum', models.CharField(max_length=20, unique=True, verbose_name='手机号')),
                ('nickname', models.CharField(max_length=32, unique=True, verbose_name='昵称')),
                ('sex', models.CharField(choices=[('male', '男性'), ('female', '女性'), ('no sex', '无')], max_length=8, verbose_name='性别')),
                ('birth_year', models.IntegerField(default=2000, verbose_name='出生年')),
                ('birth_month', models.IntegerField(default=1, verbose_name='出生月')),
                ('birth_day', models.IntegerField(default=1, verbose_name='出生日')),
                ('avatar', models.CharField(max_length=256, verbose_name='个人形象url')),
                ('location', models.CharField(max_length=16, verbose_name='常居住地')),
            ],
        ),
    ]
