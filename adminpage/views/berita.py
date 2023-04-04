from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.utils import timezone
from adminpage.views.adminpage import LoginAksesMixin, admin_only
from adminpage.models import *
from adminpage.forms.berita import *


@admin_only
def index(request):  
  context = {}

  # ===[Fetch Data]===        
  context['beritas'] = Berita.objects.all()

  # ===[Render Template]===
  context['sidebar'] = 'berita'
  context['page'] = 'berita.index'
  return render(request, 'berita/index.html', context)

@admin_only
def add(request):
  context = {}    
  # ===[Fetch Data]===    

  # ===[Load Form]===
  context['form'] = FormBerita(request.POST or None, request.FILES or None)

  if request.POST:        
    if context['form'].is_valid():  
      context['form'].save()
      messages.success(request, 'Data berhasil ditambahkan!')
      return redirect('adminpage:berita.index')        
    # else:
    #   messages.error(request, context['form'].errors)
    #   return redirect('adminpage:berita.add')


  # ===[Render Template]===
  context['sidebar'] = 'berita'
  context['page'] = 'berita.index'
  return render(request, 'berita/add.html', context)


@admin_only
def edit(request, id):
    context = {}

    # ===[Check ID IsValid]===
    try:
        getperiode = Berita.objects.get(id=id)
    except Berita.DoesNotExist:
        messages.error(request, 'Data tidak ditemukan!')
        return redirect('adminpage:berita.index')    

    # ===[Load Form]===
    context['form'] = FormBerita(request.POST or None, request.FILES or None, instance=getperiode)    

    # ===[Editt Logic]===
    if request.POST:
        
        if context['form'].is_valid():                            
            context['form'].save()            
            messages.success(request, 'Data berhasil diupdate')
            return redirect('adminpage:berita.index')            
        else:
            messages.error(request, context['form'].errors)
            return redirect('adminpage:berita.edit', id=id)

    # ===[Render Template]===
    context['sidebar'] = 'berita'
    context['page'] = 'berita.index'
    return render(request, 'berita/edit.html', context)


@admin_only
def delete(request, id):
    try:
        Berita.objects.get(id=id).delete()
        messages.success(request, 'Data berhasil dihapus')
    except Berita.DoesNotExist:
        messages.error(request, 'Data tidak ditemukan!')

    # ===[Redirect]===
    return redirect('adminpage:berita.index')