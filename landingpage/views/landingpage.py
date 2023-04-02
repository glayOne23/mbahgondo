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

  # ===[Load Form]===
  context['form'] = FormPeminat(request.POST or None, request.FILES or None)

  # ===[POST]===      
  if request.POST:
    if context['form'].is_valid():  
      context['form'].save()
      messages.success(request, 'Selamat! Mohon check pesan whatsapp anda untuk melihat harga khusus')      
      return redirect(reverse('landingpage:beranda')+"#registration")        
    else:
      print(context['form'].errors)      

  # ===[Render Template]===
  context['page'] = 'beranda'
  return render(request, 'landingpage/beranda.html', context)