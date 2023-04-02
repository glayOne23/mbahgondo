# Generated by Django 4.1.7 on 2023-04-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0004_alter_kategorimenu_gambar_menu_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peminat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('no_wa', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='kategoris',
            field=models.ManyToManyField(blank=True, to='adminpage.kategorimenu'),
        ),
    ]
