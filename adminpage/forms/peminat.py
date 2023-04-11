from django import forms
from adminpage.models import Peminat, IsianPeminatCaraMenemukan


class FormPeminat(forms.ModelForm):
  class Meta:
    model = Peminat
    fields = ['nama', 'no_wa', 'alamat', 'jumlah_kebutuhan', 'waktu_kebutuhan', 'cara_menemukan']
    labels = {      
      'nama': 'Nama',
      'no_wa': 'Nomor Whatsapp: (Contoh +628123223232)',
      'alamat': 'Alamat',
      'cara_menemukan': 'Bagaimana anda menemukan kami?',
      'jumlah_kebutuhan': 'Jumlah kebutuhan:',      
      'waktu_kebutuhan': 'Bebek Per-'
    }    

class FormIsianPeminatCaraMenemukan(forms.ModelForm):
  class Meta:
    model = IsianPeminatCaraMenemukan
    fields = ['isian']
    labels = {
      'isian': 'Cara menemukan lainnya',
    }
