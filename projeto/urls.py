from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('recipes.urls')),
    # # subdominio dominio.com/recipes/
    # path('recipes/', include('recipes.urls')),
]
