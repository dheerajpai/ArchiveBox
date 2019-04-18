# Generated by Django 2.2 on 2019-04-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='bookmarked',
        ),
        migrations.AlterField(
            model_name='page',
            name='timestamp',
            field=models.CharField(default=None, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]