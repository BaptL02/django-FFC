# Generated by Django 4.1.4 on 2023-05-29 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0050_alter_qcm_reponse_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleve',
            name='autorisation_P2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eleve',
            name='score_P2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
