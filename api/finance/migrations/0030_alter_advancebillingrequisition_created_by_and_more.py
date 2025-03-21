# Generated by Django 4.2.10 on 2025-03-05 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_company_ifsc'),
        ('finance', '0029_alter_advancebillingrequisition_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancebillingrequisition',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to='user.userrole'),
        ),
        migrations.AlterField(
            model_name='advancebillingrequisition',
            name='sales_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_owner', to='user.userrole'),
        ),
    ]
