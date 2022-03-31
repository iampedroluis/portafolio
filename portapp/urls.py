from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from portapp import views


app_name = "portfolio"

urlpatterns = [

    path('', views.home, name='home'),
    path('project/<int:project_id>', views.project_detail, name='project_detail'),
    path('contact/', views.enviarcorreo, name='enviarcorreo'),
    path('gracias/', views.gracias, name='gracias'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)