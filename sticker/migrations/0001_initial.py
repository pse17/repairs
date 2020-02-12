# Generated by Django 3.0.2 on 2020-01-30 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(blank=True, max_length=80, null=True)),
                ('invent_number', models.CharField(blank=True, max_length=18, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=24, null=True)),
                ('production_date', models.CharField(blank=True, max_length=4, null=True)),
                ('malfunction', models.TextField(blank=True, null=True)),
                ('delivery_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-delivery_date'],
                'permissions': (('can_make_sticker', 'Can make sticker'),),
            },
        ),
    ]
