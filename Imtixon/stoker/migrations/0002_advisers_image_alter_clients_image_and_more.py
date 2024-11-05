# Generated by Django 5.1 on 2024-08-18 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stoker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisers',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
