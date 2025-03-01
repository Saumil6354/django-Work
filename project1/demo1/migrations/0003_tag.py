# Generated by Django 4.0.6 on 2022-08-04 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('tag_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
