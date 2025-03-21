# Generated by Django 4.2.10 on 2024-08-01 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Project Initiated', 'Project Initiated'), ('To Be Started', 'To Be Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('On Hold', 'On Hold')], default='Project Initiated', max_length=20),
        ),
    ]
