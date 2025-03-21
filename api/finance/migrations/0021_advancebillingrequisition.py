# Generated by Django 4.2.10 on 2025-02-06 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0045_notification_notification_type'),
        ('user', '0003_company_account_number_company_account_title_and_more'),
        ('finance', '0020_vpr_other_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvanceBillingRequisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_address', models.TextField(blank=True, null=True)),
                ('contact_person_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_person_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cc_emails', models.TextField(blank=True, help_text='Comma-separated emails', null=True)),
                ('specific_billing_instruction', models.TextField(blank=True, null=True)),
                ('total_project_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('advance_invoice_percentage', models.DecimalField(blank=True, decimal_places=2, help_text='Percentage', max_digits=5, null=True)),
                ('advance_invoice_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('status', models.CharField(choices=[('Advanced Billing Raised', 'Advanced Billing Raised'), ('Advanced Invoice Generated', 'Advanced Invoice Generated'), ('Advance Payment Received', 'Advance Payment Received')], default='Advanced Billing Raised', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.client')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to='user.userrole')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.project')),
                ('project_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_manager', to='user.userrole')),
                ('sales_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_owner', to='user.userrole')),
            ],
        ),
    ]
