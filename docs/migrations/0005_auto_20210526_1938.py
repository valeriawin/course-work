# Generated by Django 3.0.12 on 2021-05-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_auto_20210526_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsrequest',
            name='docsgroup',
            field=models.CharField(max_length=20),
        ),
    ]
