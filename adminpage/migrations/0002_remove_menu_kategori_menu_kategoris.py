# Generated by Django 4.1.7 on 2023-04-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='kategori',
        ),
        migrations.AddField(
            model_name='menu',
            name='kategoris',
            field=models.ManyToManyField(null=True, to='adminpage.kategorimenu'),
        ),
    ]