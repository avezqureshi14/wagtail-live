# Generated by Django 3.2.4 on 2021-06-22 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0002_alter_blogpage_channel_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpage",
            name="last_update_at",
        ),
    ]