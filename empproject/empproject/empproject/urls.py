from django.contrib import admin
from django.urls import path
from myapp.views import createEmp,show
urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp', createEmp),
    path('show/', show),
]
