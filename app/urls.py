from django.urls import path
from app import views

urlpatterns=[
########### courier side ###########################1234567890
path('',views.index),
path('about/',views.about),
path('blog-details/',views.blogd),
path('blog/',views.blog),
path('contact/',views.contact),
path('index-2/',views.index2),
path('index3/',views.index3),
path('index4/',views.index4),
path('index5/',views.index5),
path('services-details/',views.servicesd),
path('services/',views.services),
path('userregistration/',views.user),
path('logout/',views.logout),
path('signin/',views.sign),
path('product/',views.product),

##### user url ##########################

path('viewuser/',views.viewuser),
path('edituser/',views.edituser),
path('deleteuser/',views.deleteuser),
path('updateuser/',views.updateuser),
path('changepass/',views.changepass),
path('forgotpass/',views.forgotpass),
path('forgetpassword/',views.forgetpassword),




####### product url ######################

path('viewproduct/',views.viewproduct),
path('edit/',views.edit),
path('delete/',views.delete),
path('update/',views.update),
path('search/',views.search),




####################### admin  side ##################################3
path('admin/',views.admin_index),
path('tables/',views.tables),
path('producttable/',views.producttable),

path('login/',views.login),
path('signup/',views.signup),
path('approve/',views.approve),
path('productapprove/',views.productapprove),
path('adminlogout/',views.adminlogout),
path('productreject/',views.productreject),


]