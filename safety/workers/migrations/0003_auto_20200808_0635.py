# Generated by Django 3.1 on 2020-08-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_worker_image_proflie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='image_proflie',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]