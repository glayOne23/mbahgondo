# misc
from functools import wraps
from django.shortcuts import  render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib.auth.forms import AuthenticationForm
# class based
from adminpage.models import *
from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from adminpage.forms.auth import FormSignIn


class DashboardAksesMixin(AccessMixin):    
    def dispatch(self, request, *args, **kwargs):                        
        if request.user.is_authenticated:
            return redirect('adminpage:dashboard')
        return super().dispatch(request, *args, **kwargs)   

class LoginAksesMixin(AccessMixin):    
    def dispatch(self, request, *args, **kwargs):                        
        if not request.user.is_authenticated:
            return redirect('adminpage:login')
        return super().dispatch(request, *args, **kwargs)              
    

def admin_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):        
        if request.user.is_authenticated:
             return function(request, *args, **kwargs)
        else:
            return redirect('adminpage:login')
  return wrap    


class LoginView(DashboardAksesMixin, View):
    def get(self, request):
        context = {}        
        context['formsignin'] = FormSignIn()
        return render(request, 'auth/login.html', context)                        

    def post(self, request):        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:                
                login(request, user)
                messages.success(request, 'Login Berhasil! Selamat datang di laman admin Mbah Gondo')
                return redirect('adminpage:dashboard')
            else:
                messages.error(request, 'Akun masih belum aktif!')
                return redirect('adminpage:login')
        else:
            messages.error(request, 'Mohon periksa kembali username dan password anda')
            return redirect('adminpage:login')        


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Anda telah berhasil logout.") 
        return redirect("adminpage:login")


@admin_only
def index(request):
  context = {}

  # ===[Fetch Data]===        
  context['peminat_count'] = len(Peminat.objects.all())
  context['kategori_menu_count'] = len(KategoriMenu.objects.all())
  context['menu_count'] = len(Menu.objects.all())

  # ===[Render Template]===
  context['sidebar'] = 'dasboard'
  context['page'] = 'dashboard'
  return render(request, 'dashboard/dashboard.html', context)