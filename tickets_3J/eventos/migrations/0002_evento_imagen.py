# Generated by Django 5.0.4 on 2024-09-12 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to='eventos/'),
        ),
    ]
