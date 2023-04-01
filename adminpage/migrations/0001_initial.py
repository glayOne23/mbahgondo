# Generated by Django 4.1.7 on 2023-04-01 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('gambar_menu', models.FileField(blank=True, null=True, upload_to='kategori/menu/')),
                ('gambar_text', models.FileField(blank=True, null=True, upload_to='kategori/text/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('keterangan', models.TextField()),
                ('harga', models.IntegerField()),
                ('gambar', models.FileField(blank=True, null=True, upload_to='menu/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('kategori', models.ManyToManyField(to='adminpage.kategorimenu')),
            ],
        ),
    ]
