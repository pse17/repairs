# Generated by Django 2.1.3 on 2019-01-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sticker', '0007_remove_sticker_court'),
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.CharField(db_index=True, max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
    ]