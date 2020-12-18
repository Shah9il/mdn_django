# Generated by Django 3.1.4 on 2020-12-18 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20201216_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(help_text="Select author's name", null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author'),
        ),
    ]