# Generated by Django 3.0.3 on 2020-03-14 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20200314_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
    ]