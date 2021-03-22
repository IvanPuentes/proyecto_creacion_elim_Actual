# Generated by Django 3.1.6 on 2021-03-17 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescripLib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('descrpicion', models.TextField(default='')),
                ('img', models.TextField(default='')),
                ('presio', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('descrpicion', models.TextField(default='')),
                ('img', models.TextField(default='')),
            ],
        ),
    ]
