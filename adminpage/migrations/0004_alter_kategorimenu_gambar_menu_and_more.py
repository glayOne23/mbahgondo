# Generated by Django 4.1.7 on 2023-04-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0003_alter_menu_kategoris'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategorimenu',
            name='gambar_menu',
            field=models.FileField(default='a', upload_to='kategori/menu/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kategorimenu',
            name='gambar_text',
            field=models.FileField(default='a', upload_to='kategori/text/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='gambar',
            field=models.FileField(default='a', upload_to='menu/'),
            preserve_default=False,
        ),
    ]