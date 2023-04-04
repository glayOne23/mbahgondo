from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from adminpage.models import *
from adminpage.forms.peminat import *


def error_404(request, exception):
  return render(request,'landingpage/error_404.html')


def beranda(request):
  context = {}

  # ===[Fetch Data]===      
  context['menu_text'] = Menu.objects.values('id', 'nama')  
  context['beritas'] = Berita.objects.filter(show_header=True)
  context['katalog_biasa'] = Katalog.objects.filter(tipe="biasa").first().file.url if len(Katalog.objects.filter(tipe="biasa")) == 1 else None  
  context['katalog_khusus'] = Katalog.objects.filter(tipe="khusus").first().file.url if len(Katalog.objects.filter(tipe="khusus")) == 1 else None

  # ===[Load Form]===
  context['form'] = FormPeminat(request.POST or None, request.FILES or None)

  # ===[POST]===      
  if request.POST:
    if context['form'].is_valid():  
      context['form'].save()
      messages.success(request, 'Selamat! Anda dapat mendownload harga khusus')            
      return redirect(reverse('landingpage:beranda')+"#registration")        
    else:
      print(context['form'].errors)      

  # ===[Render Template]===
  context['page'] = 'beranda'
  return render(request, 'landingpage/beranda.html', context)


def about(request):
  context = {}

  # ===[Render Template]===
  context['page'] = 'about'
  return render(request, 'landingpage/about.html', context)