from django import forms
from adminpage.models import Peminat


class FormPeminat(forms.ModelForm):
  class Meta:
    model = Peminat
    fields = ['nama', 'no_wa']
    # labels = {      
    #   'nama': _('Nama'),
    #   'tahun': _('Tahun'),
    #   'type': _('Tipe Laporan'),
    #   'status': _('Status Periode'),
    #   # 'template': _('Template'),
    # }    
