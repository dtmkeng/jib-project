# Generated by Django 3.1 on 2020-08-08 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='image_proflie',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]
