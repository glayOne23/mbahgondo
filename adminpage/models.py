from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
TIPE_KATALOG = (
    ('biasa', 'biasa'),
    ('khusus', 'khusus'),
)

class KategoriMenu(models.Model):    
    nama = models.CharField(max_length=255)    
    gambar_menu = models.FileField(upload_to='kategori/menu/')
    gambar_text = models.FileField(upload_to='kategori/text/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)    

    def __str__(self):
        return self.nama
    

class Menu(models.Model):    
    nama = models.CharField(max_length=255)
    keterangan = models.TextField()
    harga = models.IntegerField()
    gambar = models.FileField(upload_to='menu/')
    kategoris = models.ManyToManyField(KategoriMenu, blank=True )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nama    
    

class Peminat(models.Model):
    nama = models.CharField(max_length=255)
    no_wa = PhoneNumberField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nama    
    

class Katalog(models.Model):
    tipe = models.CharField(choices=TIPE_KATALOG, max_length=255, unique=True)
    file = models.FileField(upload_to='katalog/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.tipe