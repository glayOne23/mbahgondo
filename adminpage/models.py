from django.db import models

# Create your models here.

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
    kategoris = models.ManyToManyField(KategoriMenu, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nama    