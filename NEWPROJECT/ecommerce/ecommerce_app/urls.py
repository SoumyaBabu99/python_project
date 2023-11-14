from django.urls import path
from .views import *


urlpatterns =[
    path('index/',index),
    path('sellerlog/',seller_log),
    path('sellerreg/',seller_reg),
    path('product/',addpro),
    path('selpro/',seller_profile),
    path('editsel/<int:id>',seller_edit),
    path('pview/',prodview),
    path('byreg/',byerreg),
    path('bylog/',byerlog),
    path('byprof/',byer_profile),
    path('byview/<item>',byer_view),
    path('wishlist/<int:id>',wishlist),
    path('wishview/',wishlist_view),
    path('del_wish/<int:id>',delete_wish),
    path('cart/<int:id>',cart),
    path('cartview/',cart_view),
    path('del_cart/<int:id>',delete_cart),
    path('cartinc/<int:id>',cartinc),
    path('cartdec/<int:id>',cartdec),
    path('buyer_address/',address),
    path('edit_buyer_addresss',edit_buyer_address),
    path('delivery_details/',details_delivery),
    path('delidis/',delivary_display),
    path('buyer_index/',buyer_index),
    
    
]

 