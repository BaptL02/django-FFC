# Generated by Django 4.1.4 on 2023-05-29 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0049_eleve_autorisation_p1_alter_eleve_score_p1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qcm',
            name='reponse_correct',
            field=models.CharField(choices=[(1, 'Reponse 1'), (2, 'Reponse 2'), (3, 'Reponse 3'), (4, 'Reponse 4')], default=1, max_length=1),
        ),
    ]
