# Generated by Django 4.1.4 on 2023-05-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0044_alter_qcm_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='qcm',
            name='reponse_correct',
            field=models.CharField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')], default=1, max_length=1),
        ),
    ]
