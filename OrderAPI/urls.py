from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.detail_view, name = "detail" ),
    path("view/" , views.display),
    #path("order/", views.order),
    path("order/", views.Orderlist.as_view()),
    path("order/<int:pk>", views.List.as_view()),

    path('serial/', views.Serial.as_view()),
    path('serial/<int:pk>', views.Single.as_view()),
    path('all/', views.all),
    path('all/<int:id>', views.one),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('manager', views.manager),
    path('throttle', views.throttle),
    path('tuser', views.throttle_user),

]