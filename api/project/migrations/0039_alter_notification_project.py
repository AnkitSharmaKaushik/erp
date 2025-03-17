# Generated by Django 4.2.10 on 2024-12-09 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0038_notification_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_notifications', to='project.project'),
        ),
    ]
