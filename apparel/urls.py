from django.urls import path
from . import views
urlpatterns = [
   path('', views.apparel_item, name='item_apparel'),
    path('apparel_item/add/', views.add_apparel, name='add_apparel'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('apparel_item/edit/<int:pk>/', views.edit_apparel, name='edit_apparel'),
    path('dashboard/delete/<int:pk>/', views.delete_apparel, name='delete_supply'),
    path('products/<int:pk>/', views.apparel_detail, name='apparel_detail'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
