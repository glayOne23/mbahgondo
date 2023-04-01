from django.urls import path, include
from django.contrib.auth.decorators import login_required

from adminpage.views import (
    adminpage,    
)

app_name= 'adminpage'

urlpatterns = [
    path('', adminpage.index, name='dashboard'),        
    path('login/', adminpage.LoginView.as_view(), name='login'),
    path('logout/', adminpage.LogoutView.as_view(), name='logout'),
    # path('menu/', include([        
    #     path('', menu.index, name='menu'),
    #     path('create/', menu.SetReviewerView.as_view(), name='menu.create'),
    #     path('<int:id>/update/', menu.SetReviewerView.as_view(), name='menu.update'),
    #     path('<int:id>/', menu.show, name='menu'),
    #     path('<int:id>/baca_pdf', menu.baca_pdf, name='buku.baca_pdf'),
    # ])),            
]

