# Generated by Django 5.0.7 on 2024-07-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('reader', 'Reader'), ('librarian', 'Librarian')], max_length=20, null=True),
        ),
    ]
