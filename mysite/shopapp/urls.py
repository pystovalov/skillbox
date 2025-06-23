from django.urls import path
from .views import shop_index, groups_list, product_list

app_name = "shopapp"
urlpatterns = [
    path("", shop_index, name="index"),
    path("groups/", groups_list, name="groups_list"),
    path("products/", product_list, name="product"),
]
