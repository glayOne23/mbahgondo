import json
from django.db import transaction
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from adminpage.models import *
from adminpage.forms.peminat import *


def error_404(request, exception):
  return render(request,'landingpage/error_404.html')


def beranda(request):
  context = {}

  # ===[Load Form]===
  context['form'] = FormPeminat(request.POST or None, request.FILES or None)  
  context['formisian'] = FormIsianPeminatCaraMenemukan(request.POST or None, request.FILES or None)  

  # ===[Fetch Data]===      
  context['menu_text'] = Menu.objects.values('id', 'nama')  
  context['beritas'] = Berita.objects.filter(show_header=True)
  context['katalog_biasa'] = Katalog.objects.filter(tipe="biasa").first().file.url if len(Katalog.objects.filter(tipe="biasa")) == 1 else None  
  context['katalog_khusus'] = Katalog.objects.filter(tipe="khusus").first().file.url if len(Katalog.objects.filter(tipe="khusus")) == 1 else None  
  context['peminat_cara_menemukan_json'] = json.dumps(list(PeminatCaraMenemukan.objects.all().values()), indent=4, sort_keys=True, default=str)  
  context['show_isian'] = 'd-none'
  
  isian_cara_menemukan = context['form']['cara_menemukan'].value()
  if isian_cara_menemukan:
    if PeminatCaraMenemukan.objects.get(id = isian_cara_menemukan).has_isian:   
      context['show_isian'] = '' 
    
  # ===[POST]===      
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
            messages.success(request, 'Selamat! Anda dapat mendownload harga khusus')            
            return redirect(reverse('landingpage:beranda')+"#registration")        
      else:    
        if context['form'].is_valid():        
            peminat = context['form'].save()        
            messages.success(request, 'Selamat! Anda dapat mendownload harga khusus')            
            return redirect(reverse('landingpage:beranda')+"#registration")            

  # ===[Render Template]===
  context['page'] = 'beranda'
  return render(request, 'landingpage/beranda.html', context)


def about(request):
  context = {}

  # ===[Render Template]===
  context['page'] = 'about'
  return render(request, 'landingpage/about.html', context)