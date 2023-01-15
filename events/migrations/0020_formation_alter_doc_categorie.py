# Generated by Django 4.1.4 on 2023-01-10 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_alter_doc_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=300)),
                ('lien', models.URLField()),
                ('image', models.ImageField(upload_to='dossier_image')),
            ],
        ),
        migrations.AlterField(
            model_name='doc',
            name='categorie',
            field=models.CharField(choices=[('FT', 'Fonctionnement du club'), ('AT', 'ATO')], default='FT', max_length=2),
        ),
    ]
