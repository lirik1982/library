# Generated by Django 5.0.7 on 2024-07-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_phone_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
