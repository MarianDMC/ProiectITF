# Generated by Django 4.2.3 on 2023-07-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_beertypes_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='beertypes',
            name='image_cover',
            field=models.CharField(default='', max_length=150),
        ),
    ]
