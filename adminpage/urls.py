from django.urls import path, include
from django.contrib.auth.decorators import login_required

from adminpage.views import (
    adminpage,
    katalog,
    menu,
    kategori_menu,
    peminat,
    berita
)

app_name= 'adminpage'

urlpatterns = [
    path('', adminpage.index, name='dashboard'),        
    path('login/', adminpage.LoginView.as_view(), name='login'),
    path('logout/', adminpage.LogoutView.as_view(), name='logout'),
    path('menu/', include([        
        path('index', menu.index, name='menu.index'),
        path('add', menu.add, name='menu.add'),
        path('edit/<int:id>', menu.edit, name='menu.edit'),
        path('delete/<int:id>', menu.delete, name='menu.delete'),
        path('kategori/', include([        
            path('index', kategori_menu.index, name='kategori_menu.index'),
            path('add', kategori_menu.add, name='kategori_menu.add'),        
            path('edit/<int:id>', kategori_menu.edit, name='kategori_menu.edit'),
            path('delete/<int:id>', kategori_menu.delete, name='kategori_menu.delete'),
        ])),            
    ])),            
    path('peminat/', include([        
        path('index', peminat.index, name='peminat.index'),
        path('add', peminat.add, name='peminat.add'),        
        path('edit/<int:id>', peminat.edit, name='peminat.edit'),
        path('delete/<int:id>', peminat.delete, name='peminat.delete'),
        path('cetak_excel', peminat.cetak_excel, name='peminat.cetak_excel'),
    ])),            
    path('katalog/', include([        
        path('index', katalog.index, name='katalog.index'),
        path('add', katalog.add, name='katalog.add'),        
        path('edit/<int:id>', katalog.edit, name='katalog.edit'),
        path('delete/<int:id>', katalog.delete, name='katalog.delete'),
    ])),    
    path('berita/', include([        
        path('index', berita.index, name='berita.index'),
        path('add', berita.add, name='berita.add'),        
        path('edit/<int:id>', berita.edit, name='berita.edit'),
        path('delete/<int:id>', berita.delete, name='berita.delete'),
    ])),    
]

