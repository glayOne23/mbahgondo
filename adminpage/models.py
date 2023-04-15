import random
import string

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify


# Create your models here.
TIPE_KATALOG = (
    ('biasa', 'biasa'),
    ('khusus', 'khusus'),
)

WAKTU_KEBUTUHAN = (
    ('hari', 'Per Hari'),
    ('minggu', 'Per Minggu'),
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
    range_harga = models.CharField(max_length=255, blank=True, null=True)
    harga = models.IntegerField()
    gambar = models.FileField(upload_to='menu/')
    kategoris = models.ManyToManyField(KategoriMenu, blank=True )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nama    
    

class PeminatCaraMenemukan(models.Model):
    nama = models.CharField(max_length=255)
    has_isian = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nama


class Peminat(models.Model):
    nama = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    no_wa = PhoneNumberField(unique=True)
    alamat = models.TextField()
    jumlah_kebutuhan = models.IntegerField()
    waktu_kebutuhan = models.CharField(max_length=255, choices=WAKTU_KEBUTUHAN)
    cara_menemukan = models.ForeignKey(PeminatCaraMenemukan, on_delete=models.SET_NULL, blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nama    
   
    def save(self, *args, **kwargs):
        created = self.pk is None        
        if created:            
            letters = string.ascii_uppercase
            id_depan = ''.join(random.choice(letters) for i in range(3))
            id_belakang = ''.join(random.choice(letters) for i in range(2))
            last_data = Peminat.objects.all().order_by('-id')
            nomor = 1 if not last_data else last_data[0].id + 1
            self.id_number = F"{id_depan}{nomor}{id_belakang}".upper()        
        super(Peminat, self).save(*args, **kwargs)        
    

class IsianPeminatCaraMenemukan(models.Model):
    isian = models.CharField(max_length=255)
    cara_menemukan = models.ForeignKey(PeminatCaraMenemukan, on_delete=models.CASCADE)
    peminat = models.ForeignKey(Peminat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.isian        
    

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

