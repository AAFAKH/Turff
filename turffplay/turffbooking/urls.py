from django.urls import path,include
from .views import *

urlpatterns = [
    path('cust',CustomerHomeView.as_view(),name='custhome'),
    path('list/<int:id>',turf_list,name='tlist'),
    path('bookturf',book_turf,name='bookturf')
]
