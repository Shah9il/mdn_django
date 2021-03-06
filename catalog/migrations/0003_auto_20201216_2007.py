# Generated by Django 3.1.4 on 2020-12-16 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_book_front_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text="Select author's name", to='catalog.Author'),
        ),
    ]
