from django.contrib import admin
from django.urls import path
from myapp import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('emp', views.createEmp, name='createEmp'),
    path('show/', views.show, name='show'),
    path('edit/<int:eid>', views.edit_employee, name='edit_employee'),
    path('update/<int:eid>', views.update_employee, name='update_employee'),
    path('delete/<int:eid>', views.delete_employee, name='delete_employee'),
]