# Generated by Django 4.1.4 on 2022-12-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
