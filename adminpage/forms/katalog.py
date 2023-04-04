from django import forms
from adminpage.models import Katalog
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
  'application/pdf',  
]


class FormKatalog(forms.ModelForm):
  class Meta:
    model = Katalog
    fields = ['tipe', 'file']
    # labels = {      
    #   'nama': _('Nama'),
    #   'tahun': _('Tahun'),
    #   'type': _('Tipe Laporan'),
    #   'status': _('Status Periode'),
    #   # 'template': _('Template'),
    # }    


  def clean(self):
      self.check_tipe()
      self.check_file()      
      return self.cleaned_data


  def check_file(self):
      
      content = self.cleaned_data.get("file")      
      
      # === JIKA FILE ADA ===          
      if content.__class__.__name__ == 'InMemoryUploadedFile' or content.__class__.__name__ == 'TemporaryUploadedFile':
        # === CHECK FORMAT ===        
        if content.content_type not in CONTENT_TYPE:
          raise forms.ValidationError(_(" Mohon periksa tipe data anda. Tipe data yang anda upload adalah %s")%(content.content_type))      
        # === CHECK UKURAN ===
        if content.size > int(MAX_UPLOAD_SIZE):
          raise forms.ValidationError(_("Mohon ukuran file dibawah %s. File sekarang berukuran %s")%(filesizeformat(MAX_UPLOAD_SIZE), filesizeformat(content.size)))

      return content
  
  def check_tipe(self):
    tipe = self.cleaned_data.get('tipe')         
    if Katalog.objects.filter(tipe=tipe).count() > 0:             
      self.add_error('tipe', F'Tipe katalog {tipe} sudah ada. Anda hanya dapat mengubah katalog tipe tersebut')