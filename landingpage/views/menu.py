from django.http import JsonResponse, HttpResponseNotFound
from django.core.serializers import serialize
from django.shortcuts import render, redirect, HttpResponse
from adminpage.models import *


def error_404(request, exception):
  return render(request,'landingpage/error_404.html')


def by_kategori(request, kategori_id):
  context = {}
  context['kategori_id'] = kategori_id
  context['katalog_biasa'] = Katalog.objects.filter(tipe="biasa").first().file.url if len(Katalog.objects.filter(tipe="biasa")) == 1 else None  

  # ===[Fetch Data]===      
  if kategori_id !=0:
    try:
      context['kategori_show'] = KategoriMenu.objects.get(id=kategori_id)
    except KategoriMenu.DoesNotExist:
      return HttpResponseNotFound("Kategori tidak ditemukan")

  if kategori_id == 0:
    context['menus'] = Menu.objects.all()
  else:    
    kategori = KategoriMenu.objects.filter(id=kategori_id)
    context['menus'] = Menu.objects.filter(kategoris__in = kategori)    
  
  context['kategoris'] = KategoriMenu.objects.all()

  # ===[Render Template]===
  context['page'] = 'menu'
  return render(request, 'landingpage/menu/index.html', context)


def json(request, id):  
    menus = Menu.objects.filter(id=id)
    if len(menus) > 0:
      menu = []
      for m in menus:
        menu.append({'nama': m.nama, 'keterangan': m.keterangan, 'range_harga': m.range_harga, 'harga': m.harga, 'gambar': m.gambar.url})

      return JsonResponse({"success": True, "data": menu}, status=200)  
    else:
      return JsonResponse({"success": False, "message": "Menu tidak ditemukan"}, status=404)