# Generated by Django 5.0.1 on 2024-04-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdy', '0013_alter_dispatch_din_alter_dispatch_dq_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inboundtruck',
            old_name='bi',
            new_name='mdesc',
        ),
        migrations.RenameField(
            model_name='inboundtruck',
            old_name='truck',
            new_name='tname',
        ),
        migrations.RemoveField(
            model_name='inboundtruck',
            name='asign',
        ),
        migrations.RemoveField(
            model_name='inboundtruck',
            name='od',
        ),
        migrations.RemoveField(
            model_name='inboundtruck',
            name='sour',
        ),
        migrations.RemoveField(
            model_name='inboundtruck',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='inboundtruck',
            name='zone',
        ),
        migrations.AddField(
            model_name='inboundtruck',
            name='awt',
            field=models.DecimalField(decimal_places=10, default=2, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inboundtruck',
            name='cno',
            field=models.BigIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inboundtruck',
            name='mcode',
            field=models.BigIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inboundtruck',
            name='ono',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
