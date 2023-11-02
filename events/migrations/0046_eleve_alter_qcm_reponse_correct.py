# Generated by Django 4.1.4 on 2023-05-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0045_qcm_reponse_correct'),
    ]

    operations = [
        migrations.CreateModel(
            name='eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CID', models.CharField(max_length=10)),
                ('prenom', models.CharField(max_length=30)),
                ('nom', models.CharField(max_length=30)),
                ('score_P1', models.IntegerField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='qcm',
            name='reponse_correct',
            field=models.IntegerField(choices=[(1, 'Reponse 1'), (2, 'Reponse 2'), (3, 'Reponse 3'), (4, 'Reponse 4')], default=1, max_length=1),
        ),
    ]
