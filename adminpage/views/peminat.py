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