# Generated by Django 5.1.2 on 2024-10-30 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0004_input_privacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='answer',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='input',
            name='doctor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
