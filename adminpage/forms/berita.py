from django import forms
from adminpage.models import Berita
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


class FormBerita(forms.ModelForm):
  class Meta:
    model = Berita
    fields = ['judul', 'gambar', 'menuju_ke', 'konten', 'show_header']
    labels = {      
      'menuju_ke': _('Menuju laman khusus (jika ada)'),
      'konten': _('Isi Berita'),
      'show_header': _('Tampilkan pada Header'),      
    }    


  def clean(self):      
      self.check_file()      
      return self.cleaned_data


  def check_file(self):      
      content = self.cleaned_data.get("gambar")      
      
      # === JIKA FILE ADA ===          
      if content.__class__.__name__ == 'InMemoryUploadedFile' or content.__class__.__name__ == 'TemporaryUploadedFile':
        # === CHECK FORMAT ===        
        if content.content_type not in CONTENT_TYPE:
          self.add_error('gambar', _("Mohon periksa tipe data anda. Tipe data yang anda upload adalah %s")%(content.content_type))          
        # === CHECK UKURAN ===
        if content.size > int(MAX_UPLOAD_SIZE):
          self.add_error('gambar', _("Mohon ukuran file dibawah %s. File sekarang berukuran %s")%(filesizeformat(MAX_UPLOAD_SIZE), filesizeformat(content.size))) 