# Generated by Django 5.0.4 on 2024-07-30 18:37

import main_app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_zoodisplayanimal'),
    ]

    operations = [
        migrations.AddField(
            model_name='veterinarian',
            name='availability',
            field=main_app.models.BooleanChoiceField(choices=[(True, 'Available'), (False, 'Not Available')], default=True),
        ),
    ]
