# Generated by Django 4.1.4 on 2023-05-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0035_alert_hyperlink_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='hyperlink_msg',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]