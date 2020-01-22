
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import contact,about,faqs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/',include('orders.urls',namespace='orders')),
    path('',include('shop.urls',namespace='shop')),
    path('conatct',contact),
    path('about',about),
    path('faqs',faqs),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
