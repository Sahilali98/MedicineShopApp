from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('salesDash',views.salesDash,name='salesDash'),
    path('pos',views.pos,name='pos'),
    path('customerManage',views.customerManage,name='customerManage'),
    path('supplierManage',views.supplierManage,name='supplierManage'),
    path('prescripProcess',views.prescripProcess,name='prescripProcess'),
    path('reportAnalytics',views.reportAnalytics,name='reportAnalytics'),
    path('setConfig',views.setConfig,name='setConfig'),
    path('inventoryManagement',views.inventoryManagement,name='inventoryManagement'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'), # with id passing as argument 
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'), # with id passing as argument
    path('updateId', views.updateId, name='updateId'), # with out id passing as argument
    path('updaterecord/<int:id>', views.updaterecord, name='updaterecord'), # with out id passing as argument
    path('reOrder', views.reOrder, name='reOrder'), # with out id passing as argument
]