# Generated by Django 5.1.2 on 2024-10-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0003_input_delete_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='privacy',
            field=models.BooleanField(default=False),
        ),
    ]
