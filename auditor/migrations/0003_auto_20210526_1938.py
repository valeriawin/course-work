# Generated by Django 3.0.12 on 2021-05-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditor', '0002_auditor_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsaudit',
            name='docsgroup',
            field=models.CharField(max_length=20),
        ),
    ]
