# Generated by Django 2.1.1 on 2018-09-11 22:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('openComment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.CharField(default=django.utils.timezone.now, max_length=2000),
            preserve_default=False,
        ),
    ]
