from django.contrib import admin
from django.urls import path

from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list/', views.countries_list),
    path('country/<int:country_id>/', views.country_page),
    path('countries-list/<str:first_letter>/', views.countries_list_by_letters),
    path('countries-list-by-languages/<str:language>/', views.countries_list_by_languages),
    path('all-languages/', views.all_languages)
]
