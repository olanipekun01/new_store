# Generated by Django 2.2 on 2023-12-23 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20231215_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
