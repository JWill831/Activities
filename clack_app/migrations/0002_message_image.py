# Generated by Django 3.0.3 on 2020-02-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clack_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
