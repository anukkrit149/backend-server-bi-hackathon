# Generated by Django 3.1.6 on 2021-02-06 23:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='images_caption',
            fields=[
                ('uploaded_at', models.DateTimeField(auto_created=True, verbose_name='Uploaded Image')),
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('caption', models.TextField(blank=True, null=True, verbose_name='Caption')),
                ('keyword', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None, verbose_name='Keywords')),
            ],
        ),
    ]
