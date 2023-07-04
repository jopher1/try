from django.urls import path,include
from . import views
 
urlpatterns = [
    path('form/',views.employee_form),
    path('list/',views.employee_list),
    path('<int:id>',views.employee_index),
    path('',views.employee_list)
   
]