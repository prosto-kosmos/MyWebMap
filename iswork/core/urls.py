from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('login', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.MyProjectLogout.as_view(), name='logout_page'),
    path('map', views.MapView.as_view(), name='map_page'),

    path('set_settings_ajax/', views.SaveUserSettingsView.as_view(), name='set_settings'),
    path('get_settings_ajax/', views.GetSettings.as_view(), name='get_settings'),
    path('get_new_data_ajax/', views.GetNewDataView.as_view(), name='get_new_data'),
]