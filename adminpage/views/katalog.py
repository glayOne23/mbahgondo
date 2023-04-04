from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.utils import timezone
from adminpage.views.adminpage import LoginAksesMixin, admin_only
from adminpage.models import *
from adminpage.forms.katalog import *


@admin_only
def index(request):  
  context = {}

  # ===[Fetch Data]===        
  context['katalogs'] = Katalog.objects.all()

  # ===[Render Template]===
  context['sidebar'] = 'katalog'
  context['page'] = 'katalog.index'
  return render(request, 'katalog/index.html', context)

@admin_only
def add(request):
  context = {}    
  # ===[Fetch Data]===    

  # ===[Load Form]===
  context['form'] = FormKatalog(request.POST or None, request.FILES or None)

  if request.POST:        
    if context['form'].is_valid():  
      context['form'].save()
      messages.success(request, 'Data berhasil ditambahkan!')
      return redirect('adminpage:katalog.index')        
    # else:
    #   messages.error(request, context['form'].errors)
    #   return redirect('adminpage:katalog.add')


  # ===[Render Template]===
  context['sidebar'] = 'katalog'
  context['page'] = 'katalog.index'
  return render(request, 'katalog/add.html', context)


@admin_only
def edit(request, id):
    context = {}

    # ===[Check ID IsValid]===
    try:
        getperiode = Katalog.objects.get(id=id)
    except Katalog.DoesNotExist:
        messages.error(request, 'Data tidak ditemukan!')
        return redirect('adminpage:katalog.index')    

    # ===[Load Form]===
    context['form'] = FormKatalog(request.POST or None, request.FILES or None, instance=getperiode)    

    # ===[Editt Logic]===
    if request.POST:
        
        if context['form'].is_valid():                            
            context['form'].save()            
            messages.success(request, 'Data berhasil diupdate')
            return redirect('adminpage:katalog.index')            
        else:
            messages.error(request, context['form'].errors)
            return redirect('adminpage:katalog.edit', id=id)

    # ===[Render Template]===
    context['sidebar'] = 'katalog'
    context['page'] = 'katalog.index'
    return render(request, 'katalog/edit.html', context)


@admin_only
def delete(request, id):
    try:
        Katalog.objects.get(id=id).delete()
        messages.success(request, 'Data berhasil dihapus')
    except Katalog.DoesNotExist:
        messages.error(request, 'Data tidak ditemukan!')

    # ===[Redirect]===
    return redirect('adminpage:katalog.index')