# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-02 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Category that closely mathces your item', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the item', max_length=75)),
                ('discription', models.TextField(help_text='Describe this item. Write something that tells about this item', max_length=1200)),
                ('how_to_use', models.TextField(max_length=1200)),
                ('available_units', models.IntegerField(help_text='How many Nos or Kgs available?')),
                ('category', models.ManyToManyField(to='items.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MRP', models.IntegerField(help_text='MRP or the rate per unit at which you want to sell')),
                ('units', models.CharField(help_text='Rate per units (eg: 500 gms or 12 Nos', max_length=75)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.Price'),
        ),
    ]