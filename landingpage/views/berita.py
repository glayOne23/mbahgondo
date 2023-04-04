from django.http import JsonResponse, HttpResponseNotFound
from django.core.serializers import serialize
from django.shortcuts import render, redirect, HttpResponse
from adminpage.models import *



def index(request):
  context = {}

  # ===[Fetch Data]===      
  context['beritas'] = Berita.objects.all()

  # ===[Render Template]===
  context['page'] = 'berita'
  return render(request, 'landingpage/berita/index.html', context)

def show(request, id, slug):
    context = {}
    try:
        # ===[Fetch Data]===      
        context['berita'] = Berita.objects.get(id=id, slug=slug)
    except Berita.DoesNotExist:
        return HttpResponseNotFound

    # ===[Render Template]===
    context['page'] = 'berita'
    return render(request, 'landingpage/berita/show.html', context)