# Generated by Django 4.2.10 on 2024-09-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0027_project_purchase_order_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
