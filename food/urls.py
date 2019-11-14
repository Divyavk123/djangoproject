from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
app_name='food'
urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.my,name='my'),
    path('logout/',views.logout,name='logout'),
    path('register/', views.register, name='register')
    # path('admin/',views.my,name='admin'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
