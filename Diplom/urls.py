from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from Shop.views import main_page, cart, empty_section, section, item
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('cart/', cart, name='cart'),
    path('empty_section/', empty_section, name='empty_section'),
    path('section/', section, name='section'),
    path('item/', item, name='item')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)