from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify


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
    

class PeminatCaraMenemukan(models.Model):
    nama = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nama     


class Peminat(models.Model):
    nama = models.CharField(max_length=255)
    no_wa = PhoneNumberField(unique=True)
    alamat = models.TextField()
    cara_menemukan = models.ForeignKey(PeminatCaraMenemukan, on_delete=models.SET_NULL, blank=True, null=True)
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
    

class Berita(models.Model):
    judul = models.CharField(max_length=255)
    gambar = models.FileField(upload_to='berita/')
    menuju_ke = models.URLField(max_length=255, blank=True, null=True)
    konten = models.TextField()
    show_header = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.judul
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.judul)
        return super().save(*args, **kwargs)    

