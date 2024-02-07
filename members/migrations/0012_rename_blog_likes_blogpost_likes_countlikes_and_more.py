# Generated by Django 4.2.9 on 2024-01-30 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0011_blog_likescount_blog_views_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='blog',
            new_name='blogPost',
        ),
        migrations.AddField(
            model_name='likes',
            name='countLikes',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]