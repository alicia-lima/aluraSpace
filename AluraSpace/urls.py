
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.galeria.urls')),
    path('', include('apps.usuarios.urls')),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


''' foi incluido a url da galeria - path('', include('galeria.urls')),
    foi icnluido a url de usuários - path('', include('usuarios.urls'))
    foi criado os arquivos de entrada de midia - (+ static(settings.MEDIA_URL, 
                                                document_root=settings.MEDIA_ROOT))

'''