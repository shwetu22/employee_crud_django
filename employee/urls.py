from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from employee.views import home
# urlpatterns = [
#     path('', home),  \,
#     path('login', login_view),
#     path('register', register_view),
#     path('findByEmail', find_by_email),
#     path('getAll', get_all_employees),
#     path('getById', get_employee_by_id),
#     path('update', update_employee),
#     path('delete', delete_employee),
    

# ]

urlpatterns = [
   path('admin/', admin.site.urls),

    path('', home),  
    path('login', views.login),
    path('register', views.register),
    path('findByEmail', views.find_by_email),
    path('getAll', views.get_all),
    path('getById', views.get_by_id),
    path('update', views.update),
    path('delete', views.delete),
]
