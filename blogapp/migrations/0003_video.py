# Generated by Django 3.0.3 on 2020-03-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20200303_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=70)),
                ('video', models.TextField(blank=True)),
                ('height', models.CharField(default=210, max_length=7)),
                ('width', models.CharField(default=315, max_length=7)),
            ],
        ),
    ]
