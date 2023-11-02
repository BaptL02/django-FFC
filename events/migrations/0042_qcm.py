# Generated by Django 4.1.4 on 2023-05-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0041_alter_event_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='QCM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2000)),
                ('reponse1', models.CharField(max_length=1000)),
                ('reponse2', models.CharField(max_length=1000)),
                ('reponse3', models.CharField(blank=True, max_length=1000)),
                ('reponse4', models.CharField(blank=True, max_length=1000)),
                ('Niveau', models.CharField(choices=[('Air Law', 'Air Law'), ('Human Performance', 'Human Performance'), ('Meteorologie', 'Meteorologie'), ('Communications', 'Communications'), ('Principles of flight', 'Principles of flight'), ('Flight Performance and Planning', 'Flight Performance and Planning'), ('Aircraft General Knowledge', 'Aircraft General Knowledge'), ('Navigation', 'Navigation')], default='P1', max_length=100)),
            ],
        ),
    ]
