from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from adminpage.models import *


def error_404(request, exception):
  return render(request,'landingpage/error_404.html')


def beranda(request):
  context = {}

  # ===[Fetch Data]===      
  context['menu_text'] = Menu.objects.values('id', 'nama')  

  # ===[Render Template]===
  context['page'] = 'beranda'
  return render(request, 'landingpage/beranda.html', context)