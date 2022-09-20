from django.urls import path
from .views import index, get_all_product

urlpatterns = [
    path('', index, name='index'),
    path('<int:id_product>', get_all_product, name='by_product'),
]
