from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
# from buku import repositories as repo


def error_404(request, exception):
  return render(request,'landingpage/error_404.html')


def index(request):
  context = {}

  # ===[Fetch Data]===      
  # context['menus'] = repo.buku.limit_revert(4)
  context['menus'] = range (4)

  # ===[Render Template]===
  context['page'] = 'menu'
  return render(request, 'landingpage/menu/index.html', context)