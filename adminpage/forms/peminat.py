from django import forms
from adminpage.models import Peminat


class FormPeminat(forms.ModelForm):
  class Meta:
    model = Peminat
    fields = ['nama', 'no_wa', 'alamat', 'cara_menemukan']
    labels = {      
      'nama': 'Nama',
      'no_wa': 'Nomor Whatsapp: (Contoh +628123223232)',
      'alamat': 'Alamat',
      'cara_menemukan': 'Bagaimana anda menemukan kami?',
      # 'template': _('Template'),
    }    
