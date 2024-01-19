
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
    path('', include('usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


''' foi incluido a url da galeria - path('', include('galeria.urls')),
    foi icnluido a url de usuários - path('', include('usuarios.urls'))
    foi criado os arquivos de entrada de midia - (+ static(settings.MEDIA_URL, 
                                                document_root=settings.MEDIA_ROOT))

'''