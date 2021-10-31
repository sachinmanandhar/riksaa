# Generated by Django 3.0 on 2021-10-27 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_auto_20211026_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rider',
            name='location',
        ),
        migrations.AddField(
            model_name='locationdata',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='online_riders', related_query_name='online_rider', to=settings.AUTH_USER_MODEL),
        ),
    ]