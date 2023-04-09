
from .import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
  #buyer side urls
  path("home",views.home,name="home"),
 
  path("about",views.about,name="about"),

  path("rateus",views.rateus,name="rateus"),
  path("comments",views.comments,name="comments"),
  path("loginseller",views.loginseller,name="loginseller"),
  path("Beds",views.Beds,name="Beds"),
  path("chairs",views.chairs,name="chairs"),
  path("sofas",views.sofas,name="sofas"),
  path("table",views.table,name="table"),
  path("shoppingcart",views.shoppingcart,name="shoppingcart"),
  #admin side urls
  path("loginadmin",views.loginadmin,name="loginadmin"),
  path("logoutadmin",views.logoutadmin,name="logoutadmin"),
  path("logoutseller",views.logoutseller,name="logoutseller"),
  path("adminhome",views.adminhome,name="adminhome"),
  path("sellerinfo",views.sellerinfo,name="sellerinfo"),
  path("threedinfo",views.threedinfo,name="threedinfo"),
  path("uploadmodel/<int:req_id>",views.uploadmodel,name="uploadmodel"),
  path('declinemodel/<int:req_id>', views.declinemodel, name='declinemodel'),
  #seller side urls
  path("signup_seller",views.signup_seller,name="signup_seller"),
  path("homepageSeller",views.homepageSeller,name="homepageSeller"),
  path("addProduct",views.addProduct,name="addProduct"),
  path("requestinfo",views.requestinfo,name="requestinfo"),
  path("orderRecords",views.orderRecords,name="orderRecords"),
  path("shipped/<int:o_id>",views.shipped,name="shipped"),
  path("delivered/<int:o_id>",views.delivered,name="delivered"),
  path("pricingTool",views.pricingTool,name="pricingTool"),
  path("seeProducts",views.seeProducts,name="seeProducts"),
  path('editProduct/<int:p_ID>', views.editProduct, name='editProduct'),
  path("requestinfo/<int:p_ID>",views.requestinfo,name="requestinfo"),
  path("request3d/<int:p_ID>",views.request3d,name="request3d"),

  path('delete/<int:p_ID>', views.destroy),
  path("checkoutform",views.checkout,name="checkout"),

  path("password_change", views.password_change, name="password_change"),
  path("password_reset", views.password_reset_request, name="password_reset"),
  path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),

]

