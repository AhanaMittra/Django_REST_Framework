# Generated by Django 3.1.2 on 2021-04-29 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='color',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
