from django.urls import path, include

urlpatterns = [
    
    path('administrador/', include('Apps.Admin.urls_api')),
    
    
]