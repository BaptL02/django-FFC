# Generated by Django 4.1.4 on 2023-05-04 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0032_livree_ordre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livree',
            options={'ordering': ['ordre']},
        ),
        migrations.AlterField(
            model_name='livree',
            name='Filtre',
            field=models.CharField(choices=[('AIB', 'AIRBUS'), ('BOE', 'BOEING'), ('LEG', 'LEGER'), ('HEL', 'HEL')], default='AIB', max_length=3),
        ),
        migrations.DeleteModel(
            name='ChoixSondage',
        ),
        migrations.DeleteModel(
            name='Sondage',
        ),
    ]
