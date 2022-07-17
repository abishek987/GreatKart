from django.urls import path
from .  import views

urlpatterns = [
    path('',views.store , name = 'store'),
    path('<slug:categorie_slug>/',views.store , name ='product_by_category'),
    path('<slug:categorie_slug>/<slug:product_slug>/',views.product_detail , name ='product_detail'),
]
