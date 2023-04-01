from django import forms
from adminpage.models import Menu, KategoriMenu
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import filesizeformat


# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = "5242880"
CONTENT_TYPE = [
  'image/png',
  'image/svg+xml',
  'image/jpeg',  
  'image/webp'
]


class FormMenu(forms.ModelForm):
  class Meta:
    model = Menu
    fields = ['nama', 'gambar', 'harga', 'keterangan', 'kategoris']
    # labels = {      
    #   'nama': _('Nama'),
    #   'tahun': _('Tahun'),
    #   'type': _('Tipe Laporan'),
    #   'status': _('Status Periode'),
    #   # 'template': _('Template'),
    # }    


  def clean(self):
      self.check_file()      
      return self.cleaned_data


  def check_file(self):
      
      content = self.cleaned_data.get("gambar")      
      
      # === JIKA FILE ADA ===          
      if content.__class__.__name__ == 'InMemoryUploadedFile' or content.__class__.__name__ == 'TemporaryUploadedFile':
        # === CHECK FORMAT ===        
        if content.content_type not in CONTENT_TYPE:
          raise forms.ValidationError(_(" Mohon periksa tipe data anda. Tipe data yang anda upload adalah %s")%(content.content_type))      
        # === CHECK UKURAN ===
        if content.size > int(MAX_UPLOAD_SIZE):
          raise forms.ValidationError(_("Mohon ukuran file dibawah %s. File sekarang berukuran %s")%(filesizeformat(MAX_UPLOAD_SIZE), filesizeformat(content.size)))

      return content
  

class FormKategoriMenu(forms.ModelForm):
  class Meta:
    model = KategoriMenu
    fields = ['nama', 'gambar_menu', 'gambar_text']
    labels = {            
      'gambar_menu': _('Gambar untuk Kategori'),
      'gambar_text': _('Gambar untuk Text Kategori'),      
    }    


  def clean(self):
      self.check_file()      
      return self.cleaned_data


  def check_file(self):
      
      contents = [self.cleaned_data.get("gambar_menu"), self.cleaned_data.get("gambar_text")]

      for content in contents:
        # === JIKA FILE ADA ===          
        if content.__class__.__name__ == 'InMemoryUploadedFile' or content.__class__.__name__ == 'TemporaryUploadedFile':
          # === CHECK FORMAT ===        
          if content.content_type not in CONTENT_TYPE:
            raise forms.ValidationError(_(" Mohon periksa tipe data anda. Tipe data yang anda upload adalah %s")%(content.content_type))      
          # === CHECK UKURAN ===
          if content.size > int(MAX_UPLOAD_SIZE):
            raise forms.ValidationError(_("Mohon ukuran file dibawah %s. File sekarang berukuran %s")%(filesizeformat(MAX_UPLOAD_SIZE), filesizeformat(content.size)))

        return content  