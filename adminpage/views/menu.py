from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.utils import timezone
from adminpage.views.adminpage import LoginAksesMixin, admin_only
from adminpage.models import *
from adminpage.forms.menu import *


@admin_only
def index(request):
  context = {}

  # ===[Fetch Data]===      
  # context['menus'] = repo.buku.limit_revert(4)
  context['menus'] = Menu.objects.all()

  # ===[Render Template]===
  context['sidebar'] = 'menu'
  context['page'] = 'menu.index'
  return render(request, 'menu/index.html', context)

@admin_only
def add(request):
  context = {}    
  # ===[Fetch Data]===    

  # ===[Load Form]===
  context['form'] = FormMenu(request.POST or None, request.FILES or None)

  if request.POST:        
    if context['form'].is_valid():  
      context['form'].save()
      messages.success(request, 'Data berhasil ditambahkan!')
      return redirect('adminpage:menu.index')        
    # else:
    #   messages.error(request, context['form'].errors)
    #   return redirect('adminpage:menu.add')


  # ===[Render Template]===
  context['sidebar'] = 'menu'
  context['page'] = 'menu.index'
  return render(request, 'menu/add.html', context)


@admin_only
def edit(request, id):
    context = {}

    # ===[Check ID IsValid]===
    try:
        getperiode = Menu.objects.get(id=id)
    except Menu.DoesNotExist:
        messages.error(request, 'Data tidak ditemukan!')
        return redirect('adminpage:menu.index')    

    # ===[Load Form]===
    context['form'] = FormMenu(request.POST or None, request.FILES or None, instance=getperiode)    

    # ===[Editt Logic]===
    if request.POST:
        
        if context['form'].is_valid():                            
            context['form'].save()            
            messages.success(request, 'Data berhasil diupdate')
            return redirect('adminpage:menu.index')            
        else:
            messages.error(request, context['form'].errors)
            return redirect('adminpage:menu.edit', id=id)

    # ===[Render Template]===
    context['sidebar'] = 'menu'
    context['page'] = 'menu.index'    
    return render(request, 'menu/edit.html', context)


@admin_only
def delete(request, id):
    try:
        Menu.objects.get(id=id).delete()
        messages.success(request, 'Data berhasil dihapus')
    except Menu.DoesNotExist:
        messages.error(request, 'Data tidak ditemukan!')

    # ===[Redirect]===
    return redirect('adminpage:menu.index')