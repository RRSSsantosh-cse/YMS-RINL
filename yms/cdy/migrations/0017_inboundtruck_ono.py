# Generated by Django 5.0.1 on 2024-04-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdy', '0016_inboundtruck_nm'),
    ]

    operations = [
        migrations.AddField(
            model_name='inboundtruck',
            name='ono',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
