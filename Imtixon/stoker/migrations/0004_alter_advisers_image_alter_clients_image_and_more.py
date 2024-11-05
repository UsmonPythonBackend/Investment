# Generated by Django 5.1 on 2024-08-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stoker', '0003_advisers_seen_clients_seen_comments_seen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisers',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.URLField(null=True),
        ),
    ]