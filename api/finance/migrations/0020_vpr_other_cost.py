# Generated by Django 4.2.10 on 2025-02-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0019_financerequest_po_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='vpr',
            name='other_cost',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
