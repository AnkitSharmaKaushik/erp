# Generated by Django 4.2.10 on 2025-02-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
