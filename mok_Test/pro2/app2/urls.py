from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.home,name='home'),
   path('usersignup/',views.usersignup,name='usersignup'),
   path('userlogin/',views.userlogin,name='userlogin'),
   path('productview/<int:pk>/',views.productview,name='product'),
   path('cart',views.cart,name='cart'),
]
if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

