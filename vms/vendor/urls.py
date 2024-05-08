from django.urls import path
from.import views
app_name='vendor'

urlpatterns=[
    path('',views.index,name="index"),
    path('staff/',views.staff,name="staff"),
    path('product/',views.product,name="product"),
    path('order/',views.order,name="order"),
    path('profile/',views.profile,name="profile"),
    path('customer_index/',views.customer_index,name="customer_index"),
    path('customer_details/',views.customer_details,name="customer_details"),
    path('customer/',views.customer,name="customer"),
    path('product_details/',views.product_details,name="product_details"),
    path('product_edit/',views.product_edit,name="product_edit"),
    path('product_delete/',views.product_delete,name="product_delete")
   
]