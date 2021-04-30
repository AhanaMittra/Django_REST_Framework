# Generated by Django 3.1.2 on 2021-04-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]