# Generated by Django 4.0.3 on 2022-04-03 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msafiri', '0002_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routes_name', models.CharField(max_length=200)),
                ('routes_created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
