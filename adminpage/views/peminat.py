import io
import xlsxwriter
import json
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.utils import timezone
from adminpage.views.adminpage import LoginAksesMixin, admin_only
from adminpage.models import *
from adminpage.forms.peminat import *


@admin_only
def index(request):  
  context = {}

  # ===[Fetch Data]===      
  # context['peminats'] = repo.buku.limit_revert(4)
  context['peminats'] = Peminat.objects.all()

  # ===[Render Template]===
  context['sidebar'] = 'peminat'
  context['page'] = 'peminat.index'
  return render(request, 'peminat/index.html', context)

@admin_only
def add(request):
  context = {}    

  # ===[Load Form]===
  context['form'] = FormPeminat(request.POST or None, request.FILES or None)
  context['form'].fields['cara_menemukan'].widget.attrs["onchange"]="showIsian(value)"
  context['formisian'] = FormIsianPeminatCaraMenemukan(request.POST or None, request.FILES or None)  

  # ===[Fetch Data]===    
  context['peminat_cara_menemukan_json'] = json.dumps(list(PeminatCaraMenemukan.objects.all().values()), indent=4, sort_keys=True, default=str)  
  context['show_isian'] = 'd-none'

  isian_cara_menemukan = context['form']['cara_menemukan'].value()
  if isian_cara_menemukan:
    if PeminatCaraMenemukan.objects.get(id = isian_cara_menemukan).has_isian:   
      context['show_isian'] = ''  
  
  if request.POST:
      if context['show_isian'] == '':
        if context['form'].is_valid():  
          peminat = context['form'].save(commit=False)                             
          if context['formisian'].is_valid():
            isian = context['formisian'].save(commit=False)                      
            isian.peminat = peminat
            isian.cara_menemukan = peminat.cara_menemukan
            peminat.save()
            isian.save() 
            messages.success(request, 'Data berhasil ditambahkan!')
            return redirect('adminpage:peminat.index')            
      else:    
        if context['form'].is_valid():        
          peminat = context['form'].save()        
          messages.success(request, 'Data berhasil ditambahkan!')
          return redirect('adminpage:peminat.index')                

  # ===[Render Template]===
  context['sidebar'] = 'peminat'
  context['page'] = 'peminat.index'
  return render(request, 'peminat/add.html', context)


@admin_only
def edit(request, id):
    context = {}

    # ===[Check ID IsValid]===
    try:
        getpeminat = Peminat.objects.get(id=id)
    except Peminat.DoesNotExist:
        messages.error(request, 'Data tidak ditemukan!')
        return redirect('adminpage:peminat.index')    
    
    # ===[Fetch Data]===    
    context['peminat_cara_menemukan_json'] = json.dumps(list(PeminatCaraMenemukan.objects.all().values()), indent=4, sort_keys=True, default=str)  
    context['show_isian'] = 'd-none'    

    # ===[Load Form]===
    context['form'] = FormPeminat(request.POST or None, request.FILES or None, instance=getpeminat)    
    context['form'].fields['cara_menemukan'].widget.attrs["onchange"]="showIsian(value)"
    try:
        getisian = IsianPeminatCaraMenemukan.objects.get(peminat=getpeminat)        
        context['formisian'] = FormIsianPeminatCaraMenemukan(request.POST or None, request.FILES or None, instance=getisian)
    except IsianPeminatCaraMenemukan.DoesNotExist:        
        context['formisian'] = FormIsianPeminatCaraMenemukan(request.POST or None, request.FILES or None)

    isian_cara_menemukan = context['form']['cara_menemukan'].value()    
    if isian_cara_menemukan:
      if PeminatCaraMenemukan.objects.get(id = isian_cara_menemukan).has_isian:   
        context['show_isian'] = ''        

    # ===[Editt Logic]===
    if request.POST:     
        if context['show_isian'] == '':   
          if context['form'].is_valid():                            
            peminat = context['form'].save(commit=False)                             
            if context['formisian'].is_valid():            
              isian = context['formisian'].save(commit=False)                                  
              isian.peminat = peminat
              isian.cara_menemukan = peminat.cara_menemukan
              peminat.save()
              isian.save()   
              messages.success(request, 'Data berhasil diupdate')
              return redirect('adminpage:peminat.index')            
          else:
            messages.error(request, context['form'].errors)
            return redirect('adminpage:peminat.edit', id=id)
        else:    
          if context['form'].is_valid():        
            peminat = context['form'].save()        
            messages.success(request, 'Data berhasil diupdate')
            return redirect('adminpage:peminat.index')         

    # ===[Render Template]===
    context['sidebar'] = 'peminat'
    context['page'] = 'peminat.index'
    return render(request, 'peminat/edit.html', context)


@admin_only
def delete(request, id):
    try:
        Peminat.objects.get(id=id).delete()
        messages.success(request, 'Data berhasil dihapus')
    except Peminat.DoesNotExist:
        messages.error(request, 'Data tidak ditemukan!')

    # ===[Redirect]===
    return redirect('adminpage:peminat.index')


@admin_only
def cetak_excel(request):
  """ Function untuk mencetak daftar peminat

  Return:
      | file .xlsx berisi daftar peminat berdasarkan tanggal surat
  """


  
  tgl_mulai = request.GET['tgl_mulai']
  tgl_akhir = request.GET['tgl_akhir']


  output = io.BytesIO()
  workbook = xlsxwriter.Workbook(output)
  worksheet = workbook.add_worksheet()

  # Get some data to write to the spreadsheet.
  data_mentah = Peminat.objects.filter(created_at__range=[tgl_mulai, tgl_akhir])
  no = 0
  data_diolah = [
    ["Nomor", "Id Number", "Tanggal Ajuan", "Nama", "Nomor Whatsapp","Alamat", "Kebutuhan", "Cara Menemukan"]
  ]
  worksheet.set_column(0, 0, 6)
  worksheet.set_column(1, 1, 18)
  worksheet.set_column(2, 2, 18)
  worksheet.set_column(3, 3, 25)
  worksheet.set_column(4, 4, 25)
  worksheet.set_column(5, 5, 40)
  worksheet.set_column(6, 6, 20)
  worksheet.set_column(7, 7, 30)  
  for row in data_mentah:
      no += 1
      temp_list = []
      temp_list.append(no)
      temp_list.append(row.id_number)
      temp_list.append(F"{row.created_at}")
      temp_list.append(row.nama)
      temp_list.append(F"{row.no_wa}")
      temp_list.append(row.alamat)
      temp_list.append(F"{row.jumlah_kebutuhan} beber per-{row.waktu_kebutuhan}")
      if row.cara_menemukan.has_isian:
        isian_data = IsianPeminatCaraMenemukan.objects.filter(peminat = row, cara_menemukan = row.cara_menemukan)
        isian = isian_data[0].isian if isian_data else ""
        temp_list.append(F"{row.cara_menemukan} - {isian}")
      else:
          temp_list.append(F"{row.cara_menemukan}")
      data_diolah.append(temp_list)
  
  # # Write some test data.
  for row_num, columns in enumerate(data_diolah):
      for col_num, cell_data in enumerate(columns):
          worksheet.write(row_num, col_num, cell_data)

  # Close the workbook before sending the data.
  workbook.close()

  # Rewind the buffer.
  output.seek(0)

  # Set up the Http response.
  filename = 'Daftar Peminat.xlsx'
  response = HttpResponse(
      output,
      content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
  )
  response['Content-Disposition'] = 'attachment; filename=%s' % filename

  return response