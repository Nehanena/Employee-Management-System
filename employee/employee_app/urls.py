
from django.urls import path
from . import views
 
app_name ='employee_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_employee, name='create_employee'),
    path('list/', views.employee_list, name='employee_list'),
    path('search/', views.search_employee, name='search_employee'),
    path('employee/<str:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employee/<str:employee_id>/update/', views.update_employee, name='update_employee'),
    path('employee/<str:employee_id>/delete/', views.delete_employee, name='delete_employee'),
    path('debug-urls/', views.debug_urls, name='debug_urls'),
]