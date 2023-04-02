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
  # ===[Fetch Data]===    

  # ===[Load Form]===
  context['form'] = FormPeminat(request.POST or None, request.FILES or None)

  if request.POST:        
    if context['form'].is_valid():  
      context['form'].save()
      messages.success(request, 'Data berhasil ditambahkan!')
      return redirect('adminpage:peminat.index')        
    # else:
    #   messages.error(request, context['form'].errors)
    #   return redirect('adminpage:peminat.add')


  # ===[Render Template]===
  context['sidebar'] = 'peminat'
  context['page'] = 'peminat.index'
  return render(request, 'peminat/add.html', context)


@admin_only
def edit(request, id):
    context = {}

    # ===[Check ID IsValid]===
    try:
        getperiode = Peminat.objects.get(id=id)
    except Peminat.DoesNotExist:
        messages.error(request, 'Data tidak ditemukan!')
        return redirect('adminpage:peminat.index')    

    # ===[Load Form]===
    context['form'] = FormPeminat(request.POST or None, request.FILES or None, instance=getperiode)    

    # ===[Editt Logic]===
    if request.POST:
        
        if context['form'].is_valid():                            
            context['form'].save()            
            messages.success(request, 'Data berhasil diupdate')
            return redirect('adminpage:peminat.index')            
        else:
            messages.error(request, context['form'].errors)
            return redirect('adminpage:peminat.edit', id=id)

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