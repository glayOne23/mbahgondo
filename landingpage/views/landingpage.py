from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
# from buku import repositories as repo


def error_404(request, exception):
  return render(request,'landingpage/error_404.html')


def beranda(request):
  context = {}

  # ===[Fetch Data]===      
  # context['bukus'] = repo.buku.limit_revert(4)

  # ===[Render Template]===
  context['page'] = 'beranda'
  return render(request, 'landingpage/beranda.html', context)