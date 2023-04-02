from django.urls import path, include
from django.contrib.auth.decorators import login_required

from landingpage.views import (
    landingpage,  
    menu  
)

app_name= 'landingpage'

urlpatterns = [
    path('', landingpage.beranda, name='beranda'),
    path('menu/', include([        
        path('kategori/<int:kategori_id>', menu.by_kategori, name='menu_by_kategori'),
        # path('create/', menu.SetReviewerView.as_view(), name='menu.create'),
        # path('<int:id>/update/', menu.SetReviewerView.as_view(), name='menu.update'),
        # path('<int:id>/', menu.show, name='menu'),        
        path('<int:id>/json', menu.json, name='menu.json'),
    ])),
    path('tentang-kami', landingpage.about, name='about'),    
]

