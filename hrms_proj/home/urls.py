from django.urls import path
from  . import views

urlpatterns =[
    path('',views.user_login,name="user_login"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('addemployee',views.addemployee,name="addemployee"),
    path('get_addemployee',views.get_addemployee,name="get_addemployee"),
    path('listemployee',views.listemployee,name="listemployee"),
    path('edit_employee/<int:id>',views.edit_employee,name="edit_employee"),
    path('get_edit_employee/<int:id>',views.get_edit_employee,name="get_edit_employee"),
    path('delete_employee/<int:id>',views.delete_employee,name="delete_employee"),
    path('expairydetails',views.expairydetails,name="expairydetails"),
    path('catogory',views.catogory,name="catogory"),
    path('get_catogory',views.get_catogory,name="get_catogory"),
    path('delete_category/<int:id>',views.delete_category,name="delete_category"),
    path('company',views.company,name="company"),
    path('get_company',views.get_company,name="get_company"),
    path('delete_company/<int:id>',views.delete_company,name="delete_company"),
    path('edit_company/<int:id>',views.edit_company,name="edit_company"),
    path('update_company',views.update_company,name="update_company"),
    # path('update_company/<int:id>',views.update_company,name="update_company"),
    path('branch',views.branch,name="branch"),
    path('get_branch',views.get_branch,name="get_branch"),
    path('delete_branch/<int:id>',views.delete_branch,name="delete_branch"),
]
