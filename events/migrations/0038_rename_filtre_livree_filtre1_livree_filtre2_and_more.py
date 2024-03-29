# Generated by Django 4.1.4 on 2023-05-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0037_remove_vmr_lien_vmr_fichier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livree',
            old_name='Filtre',
            new_name='Filtre1',
        ),
        migrations.AddField(
            model_name='livree',
            name='Filtre2',
            field=models.CharField(choices=[('AIB', 'AIRBUS'), ('BOE', 'BOEING'), ('LEG', 'LEGER'), ('HEL', 'HEL')], default='AIB', max_length=3),
        ),
        migrations.AddField(
            model_name='livree',
            name='Filtre3',
            field=models.CharField(choices=[('AIB', 'AIRBUS'), ('BOE', 'BOEING'), ('LEG', 'LEGER'), ('HEL', 'HEL')], default='AIB', max_length=3),
        ),
    ]
