# Generated by Django 4.0.3 on 2022-04-03 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msafiri', '0004_companies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companies',
            old_name='routes_created_time',
            new_name='companies_created_time',
        ),
    ]
