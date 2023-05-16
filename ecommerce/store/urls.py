from django.urls import path
from . import views

from store.controller import authview , cart,wishlist , checkout, order

urlpatterns = [
    # path('',views.home,name="/"),
    path('',views.home,name="home"),
    path ('collections',views.collections, name="collections"),
    path ('collections/<str:slug>',views.collectionsviews, name="collectionsviews"),
    path ('collections/<str:cate_slug>/<str:prod_slug>',views.productview, name="productview"),
    path('register/', authview.register , name = "register"),
    path('login/', authview.loginpage , name = "loginpage"),
    path('logout/', authview.logoutpage , name = "logout"),
    path('add-to-cart', cart.addtocart , name = "addtocart"),
    path('cart', cart.viewcart , name = "cart"),
     path('update-cart', cart.updatecart , name = "updatecart"),
     path('delete-cart-item', cart.deletecartitem , name = "deletecartitem"),
     path('wishlist', wishlist.index , name = "wishlist"),
     path('add-to-wishlist', wishlist.addtowishlist , name = "addtowishlist"),
     path('delete-wishlist-item', wishlist.deletewishlistitem , name = "deletewishlistitem"),
    path('checkout', checkout.index , name = "checkout"), 
    path('place-order', checkout.placeorder , name = "placeorder"), 
    path('my-orders', order.index , name = "myorders"), 
    path ('view-order/<str:t_no>',order.vieworder, name="orderview"),
    path('product-list', views.productListAjax), 
     path('searchproduct', views.searchproduct , name = "searchproduct"), 
     path('contact', views.contact , name = "contact"), 
    # path('scrape/', views.scrape_and_save, name='scrape_and_save'),
    #  path ('collections/<str:cate_slug>/<str:prod_slug>',views.productview, name="Ebay"),
     path('scrape/', views.scrape_products, name='scrape_products'),
 ]