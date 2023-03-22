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
        path('', menu.index, name='menu'),
        # path('create/', menu.SetReviewerView.as_view(), name='menu.create'),
        # path('<int:id>/update/', menu.SetReviewerView.as_view(), name='menu.update'),
        # path('<int:id>/', menu.show, name='menu'),
        # path('<int:id>/baca_pdf', menu.baca_pdf, name='buku.baca_pdf'),
    ])),            
]

