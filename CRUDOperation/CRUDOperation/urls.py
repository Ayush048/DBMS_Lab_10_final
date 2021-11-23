"""CRUDOperation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showhome,name = "showhome"),
    path('emp',views.showemp,name = "showemp"),
    path('cus',views.showcus,name = "showcus"),
    path('Insert_cus',views.Insertcus,name = "Insertcus"),
    path('Insert',views.Insertemp,name = "Insertemp"),
    path('edit/<int:employee_id>',views.editemp,name = "editemp"),
    path('edit_cus/<int:customer_id>',views.editcus,name = "editcus"),
    path('update/<int:employee_id>',views.updateemp,name = "updateemp"),
    path('update_cus/<int:customer_id>',views.updatecus,name = "updatecus"),
    path('delete/<int:employee_id>',views.delemp,name = "delemp"),
    path('delete_cus/<int:customer_id>',views.delcus,name = "delcus"),
]
 