# Generated by Django 4.1.4 on 2023-05-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0047_alter_qcm_reponse_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='score_P1',
            field=models.IntegerField(null=True),
        ),
    ]
