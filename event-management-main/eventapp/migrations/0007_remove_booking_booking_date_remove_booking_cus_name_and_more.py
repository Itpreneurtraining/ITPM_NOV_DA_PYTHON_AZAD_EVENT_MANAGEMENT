# Generated by Django 5.2 on 2025-05-09 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0006_teammember'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='cus_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='cus_ph',
        ),
        migrations.AddField(
            model_name='booking',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eventapp.event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_price',
            field=models.CharField(default='Free', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booked_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
