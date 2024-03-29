# Generated by Django 4.1.4 on 2023-01-13 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_remove_vote_choice_remove_vote_poll_delete_choice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sondage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChoixSondage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choix', models.CharField(max_length=255)),
                ('votes', models.IntegerField(default=0)),
                ('sondage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.sondage')),
            ],
        ),
    ]
