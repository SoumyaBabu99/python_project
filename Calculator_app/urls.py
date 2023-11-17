from django.urls import path
from .views import *

urlpatterns=[
    path('first/',first),
    path('second/',second),
    path('third/',third),
    path('fourth/',fourth),
    path('reg_form/',reg_form),
    path('login/',login),
    path('home/',home),
    path('file/',file),
    path('emp_reg/',emp_reg),
    path('emp_search/',emp_search),
    path('product/',product),
    path('pro_search/',pro_search),
    path('upload_files/',upload_files),
    path('select/',check_select),
    path('display/',display),
    path('empdis/',empdis),
    path('filedis/',filedis),
    path('uploaddis/',uploaddis),
    path('editprofile/<int:id>',update_data),
    path('empprofile/<int:id>',update_emp),
    path('imgedit/<int:id>',img_edit),
    path('filesedit/<int:id>',files_edit),
    path('delete/<int:id>',profile_delete),
    path('authuserreg/',userregistration),
    path('auth/',userregis),
    # path('userlog/',custom_login),
    # path('register/',register.as_view(),name='register'),
    # path('login/',login.as_view(),name='login')

]

