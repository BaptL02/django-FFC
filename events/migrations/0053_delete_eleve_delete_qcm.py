# Generated by Django 4.1.4 on 2023-11-02 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0052_alter_eleve_score_p1_alter_eleve_score_p2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='eleve',
        ),
        migrations.DeleteModel(
            name='QCM',
        ),
    ]