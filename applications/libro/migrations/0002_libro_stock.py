# Generated by Django 5.0.4 on 2024-04-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='stock',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
