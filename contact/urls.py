from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.home_view, name='index'),
    path('search/', views.search, name='search'),

    # Contact (crud)
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
]
