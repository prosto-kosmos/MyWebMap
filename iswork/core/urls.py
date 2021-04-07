from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.MyProjectLogout.as_view(), name='logout_page'),
    path('map', views.MapView.as_view(), name='map_page'),
    path('userdata_save_ajax/', views.SaveUserDataView.as_view(), name='userdata_save'),
    path('get_coor_ajax/', views.GetCoorView.as_view(), name='get_coor'),
]