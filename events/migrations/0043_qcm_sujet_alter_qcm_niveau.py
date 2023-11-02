# Generated by Django 4.1.4 on 2023-05-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0042_qcm'),
    ]

    operations = [
        migrations.AddField(
            model_name='qcm',
            name='SUJET',
            field=models.CharField(choices=[('Air Law', 'Air Law'), ('Human Performance', 'Human Performance'), ('Meteorologie', 'Meteorologie'), ('Communications', 'Communications'), ('Principles of flight', 'Principles of flight'), ('Flight Performance and Planning', 'Flight Performance and Planning'), ('Aircraft General Knowledge', 'Aircraft General Knowledge'), ('Navigation', 'Navigation')], default='P1', max_length=100),
        ),
        migrations.AlterField(
            model_name='qcm',
            name='Niveau',
            field=models.CharField(choices=[('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4')], default='P1', max_length=2),
        ),
    ]
