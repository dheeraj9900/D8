# Generated by Django 4.2.9 on 2024-01-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
