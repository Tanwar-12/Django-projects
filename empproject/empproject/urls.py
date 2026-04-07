from django.contrib import admin
from django.urls import path
from myapp.views import createEmp,show,edit,update,delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp', createEmp),
    path('show/', show),
    path('edit/<str:eid>', edit),
    path('update/<str:eid>', update),
    path('delete/<str:eid>', delete),


]
